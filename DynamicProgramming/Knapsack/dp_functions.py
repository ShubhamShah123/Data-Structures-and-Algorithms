################################## 0 - 1 KNAPSACK ##################################
# KNAPSACK : RECURSIVE VERSION 
def KnapsackRecursion(weights, values, W, N):    
    # Base Condtion
    if N == 0 or W == 0:
        return 0
    
    # Choice Diagram
    # wt of item <= W
    if weights[N-1] <= W:
        return max(values[N-1] +\
                    KnapsackRecursion(weights, values,W-weights[N-1], N-1), \
                    KnapsackRecursion(weights, values,W, N-1))
    # wt of item > W
    elif weights[N-1] > W:
        return KnapsackRecursion(weights, values, W, N-1)

    return 0

# KNAPSACK : MEMOIZED VERSION 
def KnapsackMemoization(weights, values, W, N, T):    
    # Base Condtion
    if N == 0 or W == 0:
        return 0
    
    if T[N][W] != -1:
        return T[N][W]
    
    # Choice Diagram
    # wt of item <= W
    if weights[N-1] <= W:
        T[N][W] = max(values[N-1] +\
                    KnapsackMemoization(weights, values,W-weights[N-1], N-1, T), \
                    KnapsackMemoization(weights, values,W, N-1, T))
    # wt of item > W
    elif weights[N-1] > W:
        T[N][W] = KnapsackMemoization(weights, values, W, N-1, T)

    return T[N][W]

# KNAPSACK : TOP DOWN VERSION 
def KnapsackTopDown(weights, values, W, N, flag=None):
    # Init the DP matrix
    t = [[0 if i == 0 or j == 0 else 0 for j in range(W+1)] for i in range(N+1)]
    print("[DP MATRIX BEFORE]\n")
    print_matrix(t)
    
    # Fill the dp matrix
    for i in range(1, N+1):
        for j in range(W+1):
            if weights[i-1] <= j:
                t[i][j] = max(values[i-1] + t[i-1][j-weights[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]

    # Printing the dp matrix
    print_matrix(t)
    
    return t[N][W]

def print_matrix(matrix):
    print("### [DP-Table] ###")
    for row in matrix:
        print(row)
    print("-"*len(matrix[0]))

# SUBSET SUM 
def SubsetSum(array, sum, flag=None):
    N = len(array)
    t = [[True if j == 0 else False for j in range(sum+1)] for i in range(N+1)]
    # print("[DP MATRIX BEFORE]:")
    # print_matrix(t)

    for i in range(1, N+1):
        for j in range(1, sum+1):
            if array[i-1] <= j: 
                t[i][j] = t[i-1][j - array[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    # print("[DP MATRIX AFTER]:")
    if flag: print_matrix(t)
    # print_matrix(t)
                
    return t[N][sum]

# EQUAL SUM PARTITION 
def EqualSumPartition(array, flag=None):
    N = len(array)
    array_sum = sum(array)
    return False if array_sum % 2 != 0 else SubsetSum(array, array_sum // 2, flag)

# COUNT SUBSETS WITH SUM 
def CountSubsetSum(array, sum, flag=None):
    N = len(array)
    t = [[1 if j == 0 else 0 for j in range(sum+1)] for i in range(N+1)]
    # print("[DP MATRIX BEFORE]:")
    # print_matrix(t)

    for i in range(1, N+1):
        for j in range(1, sum+1):
            if array[i-1] <= j: 
                t[i][j] = t[i-1][j - array[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    if flag: print_matrix(t)
    return t[N][sum]

# MINIMNUM SUM SUBSET DIFFERENCE 
def MinimumSubsetSumDifference(array, flag=None):
    import sys
    maxSum = sum(array)
    N = len(array)
    t = [[True if j == 0 else False for j in range(maxSum+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, maxSum+1):
            if array[i-1] <= j: 
                t[i][j] = t[i-1][j - array[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    if flag: print_matrix(t)
    output = []
    for i in range(len(t[N])//2):
        if t[N][i] == True:
            output.append(i)

    minValue = sys.maxsize

    for i in range(len(output)):
        minValue = min(minValue, maxSum - 2 * output[i])

    return minValue

# COUNT SUBSET DIFFERENCE 
def CountSubsetDifference(array, difference):
    if sum(array) < difference: return 0
    temp_sum = difference + sum(array)
    if temp_sum % 2 != 0:
        return 0
    else:
        return CountSubsetSum(array, temp_sum // 2)
    

################################## UNBOUNDED KNAPSACK ##################################
# Rod Cutting
def RodCutting(price, N, maxLength, length=None, flag=None):
    if not length:
        length = list(range(1, N + 1))  # Generate length array dynamically
    else:
        length = length
    print(f"Length Array: {length}\nPrice Array: {price}\nMaxLength: {maxLength}")
    
    # Initialize DP table
    t = [[0 for _ in range(maxLength + 1)] for _ in range(N + 1)]
    
    
    if flag: print_matrix(t)
    
    for i in range(1, N + 1):
        for j in range(maxLength + 1):
            if length[i - 1] <= j:
                t[i][j] = max(price[i - 1] + t[i][j - length[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    
    if flag: print_matrix(t)
    
    return t[N][maxLength]  # Return the maximum profit

# Coin Change 1
def CoinChangeWays(coins, N, target_sum, flag=None):
    # Initialize the table with base cases
    t = [[1 if j == 0 else 0 for j in range(target_sum + 1)] for i in range(N + 1)]
    print("### INIT ####")
    if flag: print_matrix(t)
    
    # Fill the rest of the table
    for i in range(1, N + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    if flag: print_matrix(t)
    
    # Return the number of ways to make the target sum using all N coins
    return t[N][target_sum]

# Coin Change 2:
def CoinChangeCoins(coins, N, target_sum, flag=None):
    # Initialize the table with base cases
    # Initializing the first row and first column
    t = [[0 if j == 0 else float('inf') if i == 0 else 0 for j in range(target_sum + 1)] for i in range(N + 1)]

    # Initializing the second row:
    for j in range(1, target_sum+1):
        if j % coins[0] == 0:
            t[1][j] = j // coins[0]
        else:
            t[1][j] = float('inf')
    if flag: print_matrix(t)

    for i in range(2, N+1):
        for j in range(1, target_sum+1):
            if coins[i-1] <= j:
                t[i][j] = min(t[i-1][j], 1 + t[i][j - coins[i-1]])
            else:
                t[i][j] = t[i-1][j]

    if flag:print_matrix(t)
    return t[N][target_sum]
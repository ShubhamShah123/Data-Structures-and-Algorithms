import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
 
array = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

output = dp.MinimumSubsetSumDifference(array, flag=0)
print(f"Minimum subset difference: {output}")
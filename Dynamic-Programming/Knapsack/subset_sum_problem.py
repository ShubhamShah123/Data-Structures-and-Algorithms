import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
sum = int(input("Enter the sum: "))
array = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

output = dp.SubsetSum(array, sum, flag=True)
print(f"Subset Sum Problem Output: {output}")
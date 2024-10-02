import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
array = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

output = dp.EqualSumPartition(array)
print(f"Equal Sum Partition: {output}")
import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
diff = int(input("Enter the difference: "))
array = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

print(f"Total number of subsets with difference: {diff} --> {dp.CountSubsetDifference(array, diff)}")
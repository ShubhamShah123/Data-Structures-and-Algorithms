from PalindromePartitionClass import PalindromePartition

palPart = PalindromePartition()

stringA = input("Enter the string: ")
t = [[-1 for _ in range(len(stringA))] for _ in range(len(stringA))]
t, numPartitions = palPart.MemoizedPartitions(stringA, 0, len(stringA)-1, t, flag=1)
print(f"Minimum number of partitions: {numPartitions}")

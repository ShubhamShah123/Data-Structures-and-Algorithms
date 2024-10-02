from PalindromePartitionClass import PalindromePartition

palPart = PalindromePartition()

stringA = input("Enter the string: ")
numPartitions = palPart.RecursionPartition(stringA, 0, len(stringA)-1)

print(f"Minimum number of partitions: {numPartitions}")

partitions = palPart.getPartitions(stringA)
print(f"Partitions: {partitions[-1]}")
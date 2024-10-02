"""
Prefix sum approach for longest subarray with sum K;
Works if the input array contains 0s or negatives.
"""

def getLengthSubarrayPrefixSum(array, size, K):
    MAXLEN = 0
    prefix_sum = 0
    PREFIXMAP = {
        0: -1
    }
    for i in range(size):
        prefix_sum += array[i]

        # Check for prefix sum
        if prefix_sum not in PREFIXMAP:
            PREFIXMAP[prefix_sum] = i

        # Check for prefix - K
        if prefix_sum - K in PREFIXMAP:
            MAXLEN = max(MAXLEN, i - PREFIXMAP[prefix_sum - K])
    return MAXLEN

N = int(input("Enter the number of elements: "))
array = [int(input(f"Enter the value of element {i}: ")) for i in range(N)]
K = int(input("Enter the value of K(Sum): "))

subarray_length = getLengthSubarrayPrefixSum(array, N, K)
print(f"Longest subarray with sum {K} is of length: {subarray_length}")
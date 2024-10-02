def getLargestSubarray(array, size, K):
    i,j, sum = 0, 0, 0
    mx = 0
    start, end = 0, 0

    while j < size:
        sum += array[j]
        if sum < K:
            j += 1
        elif sum == K:
            mx = max(mx, j-i+1)
            start, end = i, j
            j += 1
            
        elif sum > K:
            while sum > K and i <= j:
                sum -= array[i]
                i += 1
            j += 1
    
    return mx, start, end

N = int(input("Enter the number of elements: "))
array = [int(input(f"Enter the value of element {i}: ")) for i in range(N)]
K = int(input("Enter the value of K(Sum): "))

output, start, end = getLargestSubarray(array, N, K)
print(f"Length of largest subarray with sum: {K} --> {output}")
print(f"Subarray with sum: {K} --> {array[start:end+1]}")
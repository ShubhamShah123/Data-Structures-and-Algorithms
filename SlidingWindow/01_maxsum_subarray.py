def maximumSubArray(array, K, size):
    sum = 0  # sum of subarrays
    maxSum = float('-inf')  # initialize to negative infinity to handle negative numbers in the array
    i, j = 0, 0  # start and end of sliding window
    start_index = 0  # to keep track of the start index of the max sum subarray

    while j < size:
        sum += array[j]  # add the current element to the sum

        # If we have hit the window size K
        if (j - i + 1) == K:
            if sum > maxSum:
                maxSum = sum
                start_index = i  # update start index of max sum subarray

            sum -= array[i]  # subtract the element going out of the window
            i += 1  # slide the window
        j += 1  # expand the window

    return maxSum, start_index, start_index + K  # return the start and end index of max sum subarray

size = int(input("Enter the number of elements in array: "))
array = [int(input(f"Enter the element {i}: ")) for i in range(size)]
K = int(input("Enter the size K: "))

maxSum, start, stop = maximumSubArray(array, K, size)
print(f"Maximum Sum of the Array ({array[start:stop]}): {maxSum}")

def getMaxSubarray(array, size, K):
    output = []
    i, j = 0, 0
    tempList = []  # Storing the elements which are max or could have been max for the current or next sliding window
    
    while j < size:
        # Calculations
        while len(tempList) > 0 and tempList[-1] < array[j]:
            tempList.pop()
        tempList.append(array[j])
        
        # Less than window size
        if (j - i + 1) < K:
            j += 1
        # Hitting the window size
        elif (j - i + 1) == K:  # changed from if to elif
            # Ans and sliding
            output.append(tempList[0])
            if tempList[0] == array[i]:
                tempList.pop(0)  # pop from front, not just pop()
            i += 1
            j += 1  # moved inside the elif block
    
    return output

# Example usage
size = int(input("Enter the number of elements in array: "))
array = [int(input(f"Enter the element {i}: ")) for i in range(size)]
K = int(input("Enter the size K: "))

output_array = getMaxSubarray(array, size, K)
print(f"Maximum of all subarray of size K: {K} --> {output_array}")

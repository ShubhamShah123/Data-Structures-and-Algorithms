def firstNegative(array, size, K):
    i, j = 0, 0
    temp_list, output_list = [], []
    while j < size:
        if array[j] < 0:
            temp_list.append(array[j])
        if (j-i+1) < K:
            j += 1
        elif (j-i+1) == K:
            if len(temp_list) == 0:
                output_list.append(0)
            else:
                output_list.append(temp_list[0])
                if array[i] == temp_list[0]:
                    temp_list.pop(0)
            i+=1
            j+=1
    return output_list

size = int(input("Enter the number of elements in array: "))
array = [int(input(f"Enter the element {i}: ")) for i in range(size)]
K = int(input("Enter the size K: "))

output_array = firstNegative(array, size, K)
print(f"First Negative Array in windows size K:{K} --> {output_array}")
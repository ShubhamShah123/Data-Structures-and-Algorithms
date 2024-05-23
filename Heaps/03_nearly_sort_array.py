import stack_functions as sf

def nearlySorted(array, n, k):
    minHeap, minTop = sf.create_stack(n)
    output_array = []
    
    # print(f"\n[NEARLY SORTED FUNCTION]\nArray: {array}, N: {n}, K: {k}")

    for _index in range(n):
        # print(f"### INDEX: {_index} | ELEMENT: {array[_index]} | [HeapTop]: {minHeap[minTop]} ###")
        # print(f"Heap Size: {sf.getStackSize(minHeap, minTop)}")
        if sf.getStackSize(minHeap, minTop)[1] == k + 1:
            minHeap, popped_element, minTop = sf.pop_from_stack(minHeap, minTop)
            output_array.append(popped_element)

        if sf.isStackEmpty(minTop):
            minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[_index])
        else:
            if  sf.getStackSize(minHeap, minTop)[1] <= k+1 and \
                sf.stack_peek(minHeap, minTop)[1] > array[_index]:
                # print("TOP > CURRENT")
                minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[_index])
            else:
                tempStack = []
                # print("TOP < CURRENT")
                minHeap, popped_element, minTop = sf.pop_from_stack(minHeap, minTop)
                output_array.append(popped_element)
                while not sf.isStackEmpty(minTop) and sf.stack_peek(minHeap, minTop)[1] < array[_index]:
                    minHeap, popped_element, minTop = sf.pop_from_stack(minHeap, minTop)
                    
                    tempStack.append(popped_element)
                    # print("[TEMPSTACK]: ", tempStack)

                minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[_index])
                
                while tempStack:
                    tempElement = tempStack.pop()
                    if  sf.getStackSize(minHeap, minTop)[1] < k+1:
                        minHeap, minTop = sf.push_to_stack(minHeap, minTop, tempElement)
                    elif sf.getStackSize(minHeap, minTop)[1] == k+1:
                        minHeap, popped_element, minTop = sf.pop_from_stack(minHeap, minTop)
                        output_array.append(popped_element)
    while not sf.isStackEmpty(minTop):
        minHeap, popped_element, minTop = sf.pop_from_stack(minHeap, minTop)
        output_array.append(popped_element)

    return output_array

# Simulated input functions (to be replaced with actual implementations)
n, array, stack, TOP = sf.get_input()
sf.stack_display(stack, TOP)

K = int(input("Enter the value of K: "))

output_array = nearlySorted(array, n, K)
print(f"\nOutput Array: {output_array}")

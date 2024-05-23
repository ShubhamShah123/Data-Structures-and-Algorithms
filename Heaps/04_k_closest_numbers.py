import stack_functions as sf

def closest_elements(array, n, K, X):
    maxHeap, maxTop = sf.createPairedStack(n)
    print(f"[MaxHeap]: {maxHeap} | TOP: {maxTop}")

    for _index in range(n):
        numDiff = (abs(array[_index] - X),array[_index])
        if sf.isStackEmpty(maxTop):
            maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, numDiff)
        else:
            if maxHeap[maxTop][0] < numDiff[0]:
                maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, numDiff)
            else:
                tempStack = []
                while not sf.isStackEmpty(maxTop) and sf.stack_peek(maxHeap, maxTop)[1][0] > numDiff[0]:
                    maxHeap, poppedElement, maxTop = sf.pop_from_stack(maxHeap, maxTop)
                    tempStack.append(poppedElement)

                if sf.getStackSize(maxHeap, maxTop)[1] < K:
                    maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, numDiff)

                while tempStack:
                    tempElement = tempStack.pop()
                    if sf.getStackSize(maxHeap, maxTop)[1] < K:
                        maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, tempElement)

    print(f"\n[Elements]: {maxHeap[:maxTop]}")
    return [value for key, value in maxHeap[:maxTop]]

n, array, stack, TOP = sf.get_input()

K = int(input("Enter the value of K: "))
X = int(input("Enter the value of X: "))

output_array = closest_elements(array, n, K, X)
print(f"K: {K} closeset elements for X: {X} --> {output_array}")


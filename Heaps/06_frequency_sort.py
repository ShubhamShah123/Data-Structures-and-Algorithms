import stack_functions as sf
from collections import Counter

def frequencySort(n, array):
    """
    Purpose: Sort the array based on the frequency of elements
    """
    HASHMAP = Counter(array).items()
    maxHeap, maxTop = sf.createPairedStack(n)
    for hash in HASHMAP:
        hashPair = (hash[1], hash[0])
        if sf.isStackEmpty(maxTop):
            maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, hashPair)
        else:
            if maxHeap[maxTop][0] > hashPair[0]:
                maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, hashPair)
            else:
                tempStack = []
                while not sf.isStackEmpty(maxTop) and sf.stack_peek(maxHeap, maxTop)[1][0] < hashPair[0]:
                    maxHeap, poppedElement, maxTop = sf.pop_from_stack(maxHeap, maxTop)
                    tempStack.append(poppedElement)
                
                maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, hashPair)

                while tempStack:
                    tempElement = tempStack.pop()
                    maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, tempElement)
    sorted_array = []
    while not sf.isStackEmpty(maxTop):
        maxHeap, hashPair, maxTop = sf.pop_from_stack(maxHeap, maxTop)
        sorted_array.extend([hashPair[1]] * hashPair[0])
    
    return sorted_array[::-1]


n, array, stack, TOP = sf.get_input()
output_array = frequencySort(n, array)
print(f"Sorted Array: {output_array}")
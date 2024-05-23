import stack_functions as sf
from collections import Counter

def getFrequentNumbers(n, array):
    HASHMAP = Counter(array).items()
    minHeap, minTop = sf.createPairedStack(n)
    for hash in HASHMAP:
        hashPair = (hash[1], hash[0]) # (Freq, number) : (hash[1], hash[0])
        if sf.isStackEmpty(minTop):
            minHeap, minTop = sf.push_to_stack(minHeap, minTop, hashPair)
        else:
            if minHeap[minTop][0] > hashPair[0]:
                minHeap, minTop = sf.push_to_stack(minHeap, minTop, hashPair)
            else:
                tempStack = []
                while not sf.isStackEmpty(minTop) and sf.stack_peek(minHeap, minTop)[1][0] < hashPair[0]:
                    minHeap, poppedElement, minTop = sf.pop_from_stack(minHeap, minTop)
                    tempStack.append(poppedElement)

                if sf.getStackSize(minHeap, minTop)[1] < K:
                    minHeap, minTop = sf.push_to_stack(minHeap, minTop, hashPair)

                while tempStack:
                    tempElement = tempStack.pop()
                    if sf.getStackSize(minHeap, minTop)[1] < K:
                        minHeap, minTop = sf.push_to_stack(minHeap, minTop, tempElement)
    # print(f"MinHeap: {minHeap} | MinTop: {minTop}")
    return [value for key, value in minHeap[:minTop]]

n, array, stack, TOP = sf.get_input()
K = int(input("Enter the value of K: "))
sf.stack_display(stack, TOP)

numbers_list = getFrequentNumbers(n, array)
print(f"K Frequent Numbers with K: {K} --> {numbers_list}")


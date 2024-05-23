import stack_functions as sf
import heapq as hq

n, array, stack, TOP = sf.get_input()
sf.stack_display(stack, TOP)

K  = int(input("Enter the value of K: "))

######### USING THE INBUILT LIBRARY ##############

# hq.heapify(array)
# sf.stack_display(array, TOP)

# print(hq.nsmallest(K, array)[K-1])

##################################################

######### USING THE STACK #############

maxHeap, maxTop = sf.create_stack(n)

for i in range(n):
    if sf.isStackEmpty(maxTop):
        maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, array[i])
    else:
        if maxHeap[maxTop] < array[i]:
            maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, array[i])
        else:
            tempStack = []
            while not sf.isStackEmpty(maxTop) and sf.stack_peek(maxHeap, maxTop)[1] > array[i]:
                maxHeap, poppedElement, maxTop = sf.pop_from_stack(maxHeap, maxTop)
                tempStack.append(poppedElement)

            if sf.getStackSize(maxHeap, maxTop)[1] < K:
                maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, array[i])

            while tempStack:
                tempElement = tempStack.pop()
                if sf.getStackSize(maxHeap, maxTop)[1] < K:
                    maxHeap, maxTop = sf.push_to_stack(maxHeap, maxTop, tempElement)
            
print(f"Kth smallest element with K: {K} is --> {maxHeap[maxTop]}")


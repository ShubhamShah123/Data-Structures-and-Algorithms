import stack_functions as sf
import heapq as hq

n, array, stack, TOP = sf.get_input()
sf.stack_display(stack, TOP)

K  = int(input("Enter the value of K: "))

######### USING THE INBUILT LIBRARY ##############

# hq.heapify(array)

# print(f"K largest elements with K = {K}: {hq.nlargest(K, array)}")

##################################################

######### MINHEAP USING STACK ##############

minHeap, minTop = sf.create_stack(n)

for index in range(n):
    if sf.isStackEmpty(minTop):
        minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[index])
    else:
        if minHeap[minTop] > array[index]:
            # If stack size is less than K, push the new element
            if sf.getStackSize(minHeap, minTop)[1] < K:
                minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[index])
        else:
            tempStack = []
            while not sf.isStackEmpty(minTop) and sf.stack_peek(minHeap, minTop)[1] < array[index]:
                minHeap, poppedElement, minTop = sf.pop_from_stack(minHeap, minTop)
                tempStack.append(poppedElement)
            
            # Push the new element if stack size is less than K
            if sf.getStackSize(minHeap, minTop)[1] < K:
                minHeap, minTop = sf.push_to_stack(minHeap, minTop, array[index])
            
            # Push back all elements from tempStack to minHeap
            while tempStack:
                tempElement = tempStack.pop()
                if sf.getStackSize(minHeap, minTop)[1] < K:
                    minHeap, minTop = sf.push_to_stack(minHeap, minTop, tempElement)

print(f"K lergest elements with K: {K} is --> {minHeap[:K]}")

                
"""
Nearest Greater element to right
Eg:
INPUT ARRAY : [1,3,0,0,1,1,2,4]
OUTPUT ARRAY: [3,4,1,1,2,2,4,-1]

3 conditions:
    1)  if stack is empty that is the last element if we are accessing there is no element to right
        so we append -1 to the output_array
    2)  we push the top of stack to output array if the stack size is > 0 and the top of stack is >
        current element. 
    3)  if top of stack is <= the current element: we keep popping the stack until the stack is empty
        or till we encounter the top stack which is >= current element
        - if the stack gets empty --> append -1 to output
        - else we append the top of stack
    4) PUSH the current element to stack so that we can process the next element
"""

import stack_functions as sf

n = int(input("Enter number of elements in array: "))
stack = sf.create_stack(n)
TOP = -1
input_array = []
output_array = []

for i in range(n):
    element = int(input(f"Enter element {i} to insert in array: "))
    input_array.append(element)

print(f"\n[INPUT ARRAY]: {input_array}")

for index in range(n-1,-1,-1):
    if sf.isEmpty(TOP):
        output_array.append(-1)
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP] > input_array[index]:
        output_array.append(stack[TOP])
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP] <= input_array[index]:
        while sf.size(stack, TOP)[1] > 0 and stack[TOP] <= input_array[index]:
            TOP, X, stack = sf.pop(stack, TOP)
        if sf.size(stack, TOP)[1] == 0:
            output_array.append(-1)
        else:
            output_array.append(stack[TOP])
    
    TOP, stack = sf.push(stack, TOP, input_array[index])

print(f"[OUTPUT ARRAY]: {output_array[::-1]}")
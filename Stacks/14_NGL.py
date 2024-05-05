"""
Nearest Greater element to left
Eg:
INPUT ARRAY : [1,3,0,0,1,1,2,4]
OUTPUT ARRAY: [-1,-1,3,3,3,3,-1]

2 changes as compared to 13_NGR:

    1)  We access the input array from left to right and store the array to the left of current element
        in the stack.
    2) No reversing of the output array.
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

for index in range(n):
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

print(f"[OUTPUT ARRAY]: {output_array}")
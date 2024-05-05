"""
Nearest Smaller element to Right
Example:
INPUT ARRAY: [4,5,2,10,8]
OUTPUT ARRAY: [2,2,-1,8,-1]

Changes:
1)  Popping the stack if current number < TOP of stack.
2)  Reversing of the output array
3)  Traversing the input from Right to Left
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
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP] < input_array[index]:
        output_array.append(stack[TOP])
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP] >= input_array[index]:
        while sf.size(stack, TOP)[1] > 0 and stack[TOP] >= input_array[index]:
            TOP, X, stack = sf.pop(stack, TOP)
        if sf.size(stack, TOP)[1] == 0:
            output_array.append(-1)
        else:
            output_array.append(stack[TOP])
    TOP, stack = sf.push(stack, TOP, input_array[index])

print(f"[OUTPUT ARRAY]: {output_array[::-1]}")


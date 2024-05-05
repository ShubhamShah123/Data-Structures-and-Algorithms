"""
Consecutive Smaller or Equal before it
Eg:
INPUT: [100, 80, 60, 70, 60, 75, 85]
OUTPUT: [1, 1, 1, 2, 1, 4, 6]

Almost similar to Nearest Greater ELement to Left.
14_NGL.py

Changes:
1)  Pushing (Element, index) to stack instead of just element
2)  Output will be appended by stack[TOP][1] as we are appending 2 things on stack
3)  We are comparing stack top value with the current element so it will be stack[TOP][i]
4)  Final Output: for looping the output array and subtracing index with the array value
"""

import stack_functions as sf

def create_stack(n):
    stack = [(None, None)] * n 
    return stack

n = int(input("Enter number of elements in array: "))
stack = create_stack(n)
TOP = -1
input_array = []
output_array = []

# print("Stack: ", stack)
for i in range(n):
    element = int(input(f"Enter element {i} to insert in array: "))
    input_array.append(element)

print(f"\n[INPUT ARRAY]: {input_array}")

for index in range(n):
    if sf.isEmpty(TOP):
        output_array.append(-1)
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] > input_array[index]: # Change 3
        output_array.append(stack[TOP][1]) # Change 2
    elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] <= input_array[index]: # Change 3
        while sf.size(stack, TOP)[1] > 0 and stack[TOP][0] <= input_array[index]: # Change 3
            TOP, X, stack = sf.pop(stack, TOP)
        if sf.size(stack, TOP)[1] == 0:
            output_array.append(-1)
        else:
            output_array.append(stack[TOP][1]) # Change 2
    
    TOP, stack = sf.push(stack, TOP, (input_array[index], index)) # Change 1

output_array = [index - output_array[index] for index in range(len(output_array))] # Change 4
print(f"[OUTPUT ARRAY]: {output_array}")
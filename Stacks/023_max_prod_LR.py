import stack_functions as sf

n = int(input("enter the number of elements: "))

def create_stack(n):
    return [(None, None)] * n, -1

input_array = []

def get_indices_left(input_array, n):
    stack, TOP = create_stack(n)
    output_array = []
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
    return [i+1 for i in output_array]

def get_indices_right(input_array, n):
    stack, TOP = create_stack(n)
    output_array = []
    for index in range(n-1,-1,-1):
        if sf.isEmpty(TOP):
            output_array.append(n)
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] > input_array[index]: # Change 3
            output_array.append(stack[TOP][1]) # Change 2
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] <= input_array[index]: # Change 3
            while sf.size(stack, TOP)[1] > 0 and stack[TOP][0] <= input_array[index]: # Change 3
                TOP, X, stack = sf.pop(stack, TOP)
            if sf.size(stack, TOP)[1] == 0:
                output_array.append(n)
            else:
                output_array.append(stack[TOP][1]) # Change 2
        
        TOP, stack = sf.push(stack, TOP, (input_array[index], index)) # Change 1
    return [i+1 for i in output_array]

def calc_prod(left_index_array, right_index_array):
    return max([r*l for r,l in zip(right_index_array, left_index_array)])

for i in range(n):
    element = int(input(f"Enter element {i} to insert in array: "))
    input_array.append(element)

print(f"\n[INPUT ARRAY]: {input_array}")

left_array = get_indices_left(input_array, n)
print(f"[LEFT ARRAY]: {left_array}")

right_array = get_indices_right(input_array, n)
print(f"[RIGHT ARRAY]: {right_array}")

print("OUTPUT: ",calc_prod(left_array, right_array) )

import stack_functions as sf

def sort_stack(stack, TOP):
    temp_stack = [None] * sf.size(stack, TOP)[0]
    temp_TOP = -1

    while not sf.isEmpty(TOP):
        TOP, temp, stack = sf.pop(stack, TOP)
        if sf.isEmpty(temp_TOP):
            temp_TOP, temp_stack = sf.push(temp_stack, temp_TOP, temp)
        
        while not sf.isEmpty(temp_TOP) and temp_stack[temp_TOP] > temp:
            TOP, stack = sf.push(stack, TOP, temp_stack[temp_TOP])
            temp_TOP, _, temp_stack = sf.pop(temp_stack, temp_TOP)
        
        temp_TOP, temp_stack = sf.push(temp_stack, temp_TOP, temp)

    return temp_stack, temp_TOP
        

n = int(input("enter the number of elements: "))

input_stack = [None] * n
input_TOP = -1

input_array = []
for i in range(n):
    element = int(input(f"Enter element {i} to insert in array: "))
    input_TOP, input_stack = sf.push(input_stack, input_TOP, element)
    input_array.append(element)

print(f"\n[INPUT ARRAY]: {input_array}")
sf.display_stack(input_stack, input_TOP)

sorted_stack, sorted_TOP = sort_stack(input_stack, input_TOP)
print("\n[SORTED STACK]:")
sf.display_stack(sorted_stack, sorted_TOP)

"""
Calculating the maximum area in a histogram.

INPUT: [6,2,5,4,5,1,6]
OUTPUT: 12

Steps:
1)  Calculate Indexs of NSL and NSR call them LEFT_ARRAY, RIGHT_ARRAY
2)  Calculate WIDTH.
    - WIDTH = RIGHT_ARRAY - LEFT_ARRAY - 1
3)  Calculate AREA
    - AREA = WIDTH * INPUT
4)  Return MAX(AREA)
"""

import stack_functions as sf

def create_stack(n):
    return [(None, None)] * n, -1

def get_index_NSL(input_array):
    # print("[GET INDEX NSL]")
    PSEUDO_INDEX = -1
    output_array = []
    stack, TOP = create_stack(len(input_array))
    for index in range(n):
        if sf.isEmpty(TOP):
            output_array.append(PSEUDO_INDEX)
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] < input_array[index]:
            output_array.append(stack[TOP][1])
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] >= input_array[index]:
            while sf.size(stack, TOP)[1] > 0 and stack[TOP][0] >= input_array[index]:
                TOP, X, stack = sf.pop(stack, TOP)
            if sf.size(stack, TOP)[1] == 0:
                output_array.append(PSEUDO_INDEX)
            else:
                output_array.append(stack[TOP][1])
        TOP, stack = sf.push(stack, TOP, (input_array[index], index))
    return output_array

def get_index_NSR(input_array):
    # print("[GET INDEX NSR]")
    PSEUDO_INDEX = len(input_array)
    stack, TOP = create_stack(len(input_array))
    output_array = []
    for index in range(n-1,-1,-1):
        if sf.isEmpty(TOP):
            output_array.append(PSEUDO_INDEX)
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] < input_array[index]:
            output_array.append(stack[TOP][1])
        elif sf.size(stack, TOP)[1] > 0 and stack[TOP][0] >= input_array[index]:
            while sf.size(stack, TOP)[1] > 0 and stack[TOP][0] >= input_array[index]:
                TOP, X, stack = sf.pop(stack, TOP)
            if sf.size(stack, TOP)[1] == 0:
                output_array.append(PSEUDO_INDEX)
            else:
                output_array.append(stack[TOP][1])
        TOP, stack = sf.push(stack, TOP, (input_array[index], index))
    return output_array[::-1]

def calc_width_rectangle(left_index_array, right_index_array):
    return [r - l - 1 for r,l in zip(right_index_array, left_index_array)]

def calc_area(width_array, input_array):
    return [w*i for w,i in zip(width_array, input_array)]

n = int(input("Enter the number of buildings: "))


building_heights = []
for i in range(n):
    height = int(input(f"Enter the height of building {i}: "))
    building_heights.append(height)

print(f"\nINPUT_ARRAY:\t{building_heights}")

left_index_array = get_index_NSL(building_heights)
# print("LEFT_INDEX_ARRAY:\t", left_index_array)
right_index_array = get_index_NSR(building_heights)
# print("RIGHT_INDEX_ARRAY:\t", right_index_array)
width_array = calc_width_rectangle(left_index_array, right_index_array)
# print("WIDTH_INDEX_ARRAY:\t", width_array)
area_array = calc_area(width_array, building_heights)
# print("AREA_ARRAY:\t", area_array)
output = max(area_array)
print(f"OUTPUT: {output}")
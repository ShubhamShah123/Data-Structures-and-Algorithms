"""
Calculaing the maximum area of rectangle in the binary matrix.
INPUT: 
[0,1,1,0]
[1,1,1,1]
[1,1,1,1]
[1,1,0,0]

OUTPUT: 8

Explanation:
Similar to MAH. How ??. In MAH we do the calculation of 1-D input arrays. But here we have the input as
2-D array.
Break down the 2-D array into 1-D and calculate the MAH of that array and then compute max of all MAH
which will be the output.

But how to convert 2D to 1D??
1) H1 = INPUT_MATRIX[1] (First row) ==> Calcualte MAH ==> mah1
2) from second row onwards:
    - H2 = H1 + INPUT_MATRIX[2] ==> Calcualte MAH ==> mah2
    - So on and so forth.
3) Calculate the max(mah1, mah2, ...) ==> OUTPUT
"""

import stack_functions as sf

def create_stack(n):
    return [(None, None)] * n, -1

def get_index_NSL(input_array):
    # print("[GET INDEX NSL]")
    PSEUDO_INDEX = -1
    output_array = []
    n = len(input_array)
    stack, TOP = create_stack(n)
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
    n = len(input_array)
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

def MAH(input_array):
    n = len(input_array)
    # Calculate NSL
    left_index_array = get_index_NSL(input_array)
    # Calculate NSR
    right_index_array = get_index_NSR(input_array)
    # Calculate the width of rectangle
    width_array = calc_width_rectangle(left_index_array, right_index_array)
    # Calculate the area of rectangle
    area_array = calc_area(width_array, input_array)
    # Get the maximum area
    output = max(area_array)
    # Return the output
    return output

def main():
    rows, columns = map(int, input('Enter the number of rows and columns: ').split())
    input_array = []
    vector = []
    for r in range(rows):  
        row = []
        for c in range(columns):  
            num = int(input(f"Enter 0 or 1 for ({r},{c}): "))  
            row.append(num)
        input_array.append(row)

    # Printing the matrix
    print("\nThe input matrix is:")
    for row in input_array:
        print(row)

    vector = input_array[0]
    max_area = MAH(vector)
    for r in range(1,rows):
        for c in range(columns):
            if input_array[r][c] == 0:
                vector[c] = 0
            else:
                vector[c] = vector[c] + input_array[r][c]
        max_area = max([max_area, MAH(vector)])
    print(f"Maximum area of Rectangle in given Binary Matrix: {max_area}")
if __name__ == "__main__":
    main()



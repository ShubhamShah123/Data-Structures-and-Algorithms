import stack_functions as sf

def get_max_left(input_array):
    maxLeft = [0]*len(input_array)
    maxLeft[0] = input_array[0]
    for i in range(len(input_array)):
        maxLeft[i] = max(maxLeft[i-1], input_array[i])
    return maxLeft

def get_max_right(input_array):
    n = len(input_array)
    maxRight = [0]*n
    maxRight[n-1] = input_array[n-1]
    for i in range(n-2,-1,-1):
        maxRight[i] = max(maxRight[i+1], input_array[i])
    return maxRight
    
def calc_units_water(input_array, size):
    maxL = get_max_left(input_array)
    maxR = get_max_right(input_array)
    water_array = [min(maxL[i], maxR[i]) - input_array[i] for i in range(N)]
    return sum(water_array)

N = int(input("Enter total number of buildings: "))
list_building_heights = [int(input(f"Enter height of building {i}: ")) for i in range(N)]
print(f"\nInput Array: {list_building_heights}")

output = calc_units_water(list_building_heights, N)
print("Total Unites of Water: ", output)
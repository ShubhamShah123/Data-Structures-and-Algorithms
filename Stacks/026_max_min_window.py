import stack_functions as sf

n, array, stack, TOP = sf.get_input()
# sf.display_stack(stack, TOP)
print(f"\nArray: {array}")
output = []
for window_length in range(1, n+1):
    temp = []
    for i in range(n - window_length + 1):
        window = array[i:i+window_length]
        temp.append(min(window))
    output.append(max(temp))
    # print(f"Window {window_length}: {temp}: {max(temp)}")
print(f"\nOutput: {output}")
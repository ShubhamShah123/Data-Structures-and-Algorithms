def get_length_balanced_paranthesis(string):
    _sum = 0
    max_index = 0
    for i in range(len(string)):
        if string[i] in ['(', '{', '[']:
            _sum += 1
        if string[i] in [')', '}', ']']:
            _sum -= 1
        if _sum < 0:
            break
        if _sum == 0:
            max_index = i 
    return max_index+1, string[:max_index+1]

par_string = input("Enter the string: ")
string_length, balanced_string = get_length_balanced_paranthesis(par_string)
print(f"Total Length of balanced string: {string_length}\nBalanced String: {balanced_string}")
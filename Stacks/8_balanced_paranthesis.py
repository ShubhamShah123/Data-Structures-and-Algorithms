import stack_functions as sf

def check_paranthesis(paranthesis_string):
    stack = [None] * len(paranthesis_string)
    TOP = -1
    for ch in paranthesis_string:
        if ch in ['(', '{', '[']:
            TOP, stack = sf.push(stack, TOP, ch)
        else:
            if sf.isEmpty(TOP):
                return False
            TOP, popped_element, stack = sf.pop(stack, TOP)
            if popped_element is None:
                return False
            if ch == ')' and popped_element != '(':
                return False
            if ch == ']' and popped_element != '[':
                return False
            if ch == '}' and popped_element != '{':
                return False
            
    return sf.isEmpty(TOP)  # Check if the stack is empty after processing all characters

paranthesis_string = input("Enter the string: ")
print(f"String: {paranthesis_string}")
result = "Balanced" if check_paranthesis(paranthesis_string) else "Not Balanced"
print(f"Result: {result}")

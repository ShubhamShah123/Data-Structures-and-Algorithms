# Program to convert infix equation to postfix equation:
'''
Infix equation: a+b*c-d
Postfix equation: abc*+d-
'''

import stack_functions as sf

OP_DICT = {
    
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

def get_precedence(c, operators=OP_DICT):
    return operators.get(c, -1)

def associativity(c):
    return 'R' if c == '^' else 'L'

# infix = "A+B–C*D/E+F"
infix = input("Enter the infix equation: ")
print(f"Infix: {infix}")

stack = [None] * len(infix)
TOP = -1
result = []

for i in range(len(infix)):
    c = infix[i]
    if c.isalnum():
        result.append(c)
    elif c == '(':
        TOP, stack = sf.push(stack, TOP, c)
    elif c == ')':
        print("[Second Elif - Closing Parenthesis]")
        while TOP != -1 and stack[TOP] != '(':
            print("[While Loop]")
            TOP, popped_character, stack = sf.pop(stack, TOP)
            result.append(popped_character)
        # Discard the opening parenthesis
        TOP, popped_character, stack = sf.pop(stack, TOP)
    elif c in OP_DICT.keys():
        if TOP == -1 or get_precedence(stack[TOP]) < get_precedence(c):
            TOP, stack = sf.push(stack, TOP, c)
            continue
        while TOP != -1 and get_precedence(stack[TOP]) >= get_precedence(c):
            TOP, popped_character, stack = sf.pop(stack, TOP)
            result.append(popped_character)
        TOP, stack = sf.push(stack, TOP, c)  # Push the current operator onto the stack

while TOP != -1:
    TOP, popped_character, stack = sf.pop(stack, TOP)
    result.append(popped_character)

print("Postfix Result: ", ''.join(result))

import stack_functions as sf

OP_DICT = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

output_string = ''

def get_precedence(c, operators=OP_DICT):
    return operators.get(c, -1)

infix = input("Enter the infix string: ")[::-1]
stack = [None] * len(infix)
TOP = -1

print(f"Infix Equation: {infix}")

for index in range(len(infix)):
    X = infix[index]
    if X == ')':
        TOP, stack = sf.push(stack, TOP, X)
    elif X == '(':
        while stack[TOP] != ')':
            TOP, popped_elem, stack = sf.pop(stack, TOP)
            output_string += popped_elem
        TOP, _, stack = sf.pop(stack, TOP)  # Discard the '(' from stack
    elif X.isalnum():
        output_string += X
    elif X in OP_DICT:
        while TOP > -1 and stack[TOP] in OP_DICT and get_precedence(X) <= get_precedence(stack[TOP]):
            _, popped_elem, stack = sf.pop(stack, TOP)
            output_string += popped_elem
        TOP, stack = sf.push(stack, TOP, X)

# Pop remaining operators from stack
while TOP > -1:
    _, popped_elem, stack = sf.pop(stack, TOP)
    output_string += popped_elem

# Reverse the output
output_string = output_string[::-1]

print("Postfix Equation:", output_string)
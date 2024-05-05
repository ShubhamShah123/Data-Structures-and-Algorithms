import stack_functions as sf

OP_DICT = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

OPERATORS = {
    '^': lambda x, y: x ** y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

def get_precedence(c, operators=OP_DICT):
    return operators.get(c, -1)

def associativity(c):
    return 'R' if c == '**' else 'L'

def get_postfix_notation(infix):
    infix = infix.split()  # Split the input by spaces
    stack = [None] * len(infix)
    TOP = -1
    result = []

    for i in range(len(infix)):

        c = infix[i]
        if c.isdigit():
            result.append(c)
        elif c == '(':
            TOP, stack = sf.push(stack, TOP, c)
        elif c == ')':
            while TOP != -1 and stack[TOP] != '(':
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

    return ' '.join(result)


def evaluate_postfix(postfix):
    stack = [None]*len(postfix.split())
    TOP = -1
    for i in postfix.split():
        if i.isdigit():
            TOP, stack = sf.push(stack, TOP, int(i))
        elif i in OP_DICT.keys():
            TOP, y, stack = sf.pop(stack, TOP)
            TOP, x, stack = sf.pop(stack, TOP)
            result = OPERATORS[i](x, y)
            TOP, stack = sf.push(stack, TOP, int(result))
    return sf.pop(stack, TOP)[1]

infix = input("Enter the infix equation to evaluate (with spaces between operands and operators): ")
postfix = get_postfix_notation(infix)
print(f"Reverse Polish (POSTFIX) Notation: {postfix}")
print(f"Solution: {evaluate_postfix(postfix)}")

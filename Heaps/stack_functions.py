def create_stack(n):
    stack = [None] * n
    return stack, -1

def createPairedStack(n):
    stack = [(None, None)]*n
    return stack, -1

def get_input():
    n = int(input("enter the number of elements: "))
    input_array = []
    input_stack, input_TOP = [None]*n, -1
    for i in range(n):
        element = int(input(f"Enter element {i} to insert in array: "))
        input_stack, input_TOP = push_to_stack(input_stack, input_TOP, element)
        input_array.append(element)
    
    return n, input_array, input_stack, input_TOP


def push_to_stack(S, TOP, X):
    if TOP >= len(S) - 1:
        print("Stack overflow!")
        return S, TOP
    
    TOP += 1
    S[TOP] = X
    return S, TOP

def stack_display(S, TOP):
    if TOP == -1:
        print("Stack is empty!")
    else:
        print(f"\nTop of the Stack: {TOP}\nElements of the stack: \n")
        print("|", end= "")
        for i in range(TOP + 1):
            print(f"{S[i]}|", end= "")
        print()

def pop_from_stack(S, TOP):
    if TOP == -1:
        print("Stack Underflow while popping!")
        return S, TOP, None
    
    TOP -= 1
    return S, S[TOP+1], TOP

def stack_peek(S, TOP):
    if TOP == -1:
        print("Stack Underflow while peeking!")
        return S, None, TOP
    else:
        return S, S[TOP], TOP

def stack_peep(S, TOP, index):
    if isStackEmpty(TOP):
        print("Stack underflow while peeking!")
        return TOP, None, S
    return S, S[index], TOP

def isStackEmpty(TOP):
    return TOP == -1

def isStackFull(TOP, size):
    return TOP == size - 1

def getStackSize(S, TOP):
    elements_count = 0
    if TOP == -1:
        return len(S), 0
    else:
        for i in range(TOP + 1):
            if S[i] is not None:
                elements_count += 1
        return len(S), elements_count
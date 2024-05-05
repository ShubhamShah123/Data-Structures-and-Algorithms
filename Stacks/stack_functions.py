
def create_stack(n):
    stack = [None] * n
    return (stack, -1)
# Function to push element onto the stack
def push(S, TOP, X):
    # Check for stack overflow
    if TOP >= len(S) - 1:
        print("Stack overflow!")
        return TOP, S
    
    # Increment TOP
    TOP += 1
    
    # Insert element
    S[TOP] = X
    
    # print(f"Element {X} pushed onto the stack!")
    return TOP, S

# Function to display elements of the stack
def display_stack(S, TOP):
    if TOP == -1:
        print("Stack is empty!")
    else:
        print(f"\nTop of the Stack: {TOP}\nElements of the stack: \n")
        print("| ", end= " ")
        for i in range(TOP + 1):
            print(f"{S[i]} |", end= " ")

# Function to pop the element from the stack
def pop(S, TOP):
    if TOP == -1:
        print("Stack Underflow while popping!")
        return TOP, None, S
    
    TOP -= 1
    return TOP, S[TOP+1], S

# Function to peek at the top of stack
def peek(S, TOP):
    if TOP == -1:
        print("Stack Underflow while peeking!")
        return TOP, None, S
    else:
        return TOP, S[TOP], S

# Function to peep at the particular index in stack
def peep(S, TOP, index):
    if isEmpty(TOP):
        print("Stack underflow while peeking!")
        return TOP, None, S
    return TOP, S[index], S

# Functions to see if the stack is empty or full:
def isEmpty(TOP):
    return TOP == -1

def isFull(TOP, size):
    return TOP == size - 1

# Function to get the size of stack
def size(S, TOP):
    elements_count = 0
    if TOP == -1:
        # print("Stack empty!")
        return 0,0
    else:
        for i in range(TOP + 1):
            if S[i] != None:
                elements_count += 1
        return len(S), elements_count

# Function to insert element at a particular index    
def insert_at_index(S, TOP, index, X):
    if TOP >= len(S) - 1:
        print("Stack overflow !! ")
        return TOP, S
    
    if index < 0 or index > TOP + 1:
        print("Indvalid Index !!")
        return TOP, S

    TOP, peeped_element, S = peep(S, TOP, index)    
    for i in range(TOP, index, -1):
        S[i+1] = S[i]

    S[index] = X
    S[index+1] = peeped_element
    TOP += 1
    print(f"Element {X} is inserted at index {index} !")
    return TOP, S

# Function to delete the element from a index
def delete_at_index(S, TOP, index):
    if isEmpty(TOP):
        print("Stack Underflow !!")
        return TOP, S

    if index < 0 or index > TOP + 1:
        print("Indvalid Index !!")
        return TOP, S
    
    delete_elem = S[index]
    # Driving code goes here
    for i in range(index, TOP):
        S[i] = S[i+1]
    
    TOP, pop_elem, S_popped = pop(S, TOP)
    print(f"Element {delete_elem} deleted from index {index} !")
    return TOP, S

# Function to search the element
def search_element(S, TOP, X):
    list_of_indices = []
    if isEmpty(TOP):
        print("Stack is Empty!")
        return []
    list_of_indices = [i+1 for i in range(TOP + 1) if S[i] == X]
    return list_of_indices


################# STACK REVERSING ##################

def create_stack(n):
    stack = [None] * n
    return stack

def insertAtBottom(stack, TOP, element):
    if TOP == -1:
        TOP, stack = push(stack, TOP, element)
    else:
        TOP, popped_element, stack = pop(stack, TOP)
        stack, TOP = insertAtBottom(stack, TOP, element)
        TOP, stack = push(stack, TOP, popped_element)
    return stack, TOP

def reverseStack(stack, TOP):
    # print("### Reverse stack function ###")
    if TOP == -1:
        return stack, TOP
    else:
        TOP, X, stack = pop(stack, TOP)
        stack, TOP = reverseStack(stack, TOP)
        stack, TOP = insertAtBottom(stack, TOP, X)
        # sf.display_stack(stack, TOP)
        return stack, TOP

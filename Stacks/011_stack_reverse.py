import stack_functions as sf

def create_stack(n):
    stack = [None] * n
    return stack

def insertAtBottom(stack, TOP, element):
    if sf.isEmpty(TOP):
        TOP, stack = sf.push(stack, TOP, element)
    else:
        TOP, popped_element, stack = sf.pop(stack, TOP)
        stack, TOP = insertAtBottom(stack, TOP, element)
        TOP, stack = sf.push(stack, TOP, popped_element)
    return stack, TOP

def reverseStack(stack, TOP):
    # print("### Reverse stack function ###")
    if sf.isEmpty(TOP):
        return stack, TOP
    else:
        TOP, X, stack = sf.pop(stack, TOP)
        stack, TOP = reverseStack(stack, TOP)
        stack, TOP = insertAtBottom(stack, TOP, X)
        # sf.display_stack(stack, TOP)
        return stack, TOP

def main():
    n = int(input("Enter number of elements in stack: "))
    stack = create_stack(10)
    TOP = -1

    for i in range(n):
        element = int(input(f"Element {i} to add to stack: "))
        TOP, stack = sf.push(stack, TOP, element)
    # print("----------------------")
    sf.display_stack(stack, TOP)

    # Function to reverse the stack
    stack, TOP = reverseStack(stack, TOP)
    sf.display_stack(stack, TOP)

if __name__ == "__main__":
    main()
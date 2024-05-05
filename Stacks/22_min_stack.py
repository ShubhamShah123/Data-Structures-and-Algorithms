import stack_functions as sf

choice = -1
stack, TOP = [None]*10, -1
minElement = -1

def stack_push(stack, TOP, X):
    print("Stack Push!")
    global minElement
    if sf.isEmpty(TOP):
        TOP, stack = sf.push(stack, TOP, X)
        minElement = X
    else:
        if X >= minElement:
            TOP, stack = sf.push(stack, TOP, X)
        elif X < minElement:
            temp = (2 * X) - minElement
            TOP, stack = sf.push(stack, TOP, temp)
            minElement = X
    return stack, TOP

def stack_pop(stack, TOP):
    print("Stack Pop!")
    global minElement
    if sf.isEmpty(TOP):
        return stack, TOP, -1
    if stack[TOP] >= minElement:
        TOP, X, stack = sf.pop(stack, TOP)
    elif stack[TOP] < minElement:
        minElement = (2 * minElement) - stack[TOP]
        TOP, X, stack = sf.pop(stack, TOP)
    return stack, TOP, X

def getMin(stack, TOP):
    print("Get Min")
    global minElement
    return -1 if sf.isEmpty(TOP) else minElement

def stack_top(stack, TOP):
    print("Stack Top")
    global minElement
    if sf.isEmpty(TOP):
        return -1
    elif stack[TOP] >= minElement:
        return stack[TOP]
    elif stack[TOP] < minElement:
        return minElement
    
while choice != 0:
    print("\n1. Push.\n2. Pop.\n3. Display.\n4. GetMin. \n5. Top.\n0. Exit.")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("Push")
        X = int(input("Enter element to push:"))
        stack, TOP = stack_push(stack, TOP, X)
    elif choice == 2:
        print("Popped Element: ", stack_pop(stack, TOP))
        
    elif choice == 3:
        print("Display")
        sf.display_stack(stack, TOP)
    elif choice == 4:
        print("Minimum Element in stack: ", getMin(stack, TOP))
    elif choice == 5:
        print("Top: ", stack_top(stack, TOP))

print("Exiting Program !")

import stack_functions as sf

choice = -1
S = [None]*10   #Stack
SS = [None]*10  #Support Stack
S_TOP = -1      #TOP of Stack
SS_TOP = -1     #TOP of Support Stack

def stack_push(element, S, S_TOP, SS, SS_TOP):
    print(f"Stack Push: {element}")
    S_TOP, S = sf.push(S, S_TOP, element)
    if sf.isEmpty(SS_TOP) or element <= SS[SS_TOP]:
        SS_TOP, SS = sf.push(SS, SS_TOP, element)
    return S, S_TOP, SS, SS_TOP

def stack_pop(S, S_TOP, SS, SS_TOP):
    print("Stack Popping!")
    if sf.isEmpty(S_TOP):
        return -1
    S_TOP, element, S = sf.pop(S, S_TOP)
    if SS[SS_TOP] == element:
        SS_TOP, X, SS = sf.pop(SS, SS_TOP)
    return element

def getMinimum(SS, SS_TOP):
    print("Get Minimum")
    return -1 if sf.isEmpty(SS_TOP) else SS[SS_TOP]


while choice != 0:
    print("\n1. Push.\n2. Get Min.\n3. Display. \n4. Pop\n0. Exit.")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        X = int(input("Enter the element to push onto the stack: "))
        S, S_TOP, SS, SS_TOP = stack_push(X,S, S_TOP, SS, SS_TOP)
    elif choice == 2:
        minElement = getMinimum(SS, SS_TOP)
        print(f"Minumum Element from the stack is: {minElement}")
    elif choice == 3:
        print("Stack: ")
        sf.display_stack(S, S_TOP)
        print("\nSupport Stack: ")
        sf.display_stack(SS, SS_TOP)

    elif choice == 4:
        ans = stack_pop(S, S_TOP, SS, SS_TOP)
        print("Popping: ", ans)
    
print("Exiting Program !")
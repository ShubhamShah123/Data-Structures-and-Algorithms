import stack_functions as sf

postfix = input("Enter Postfix Equation: ")
stack = [None] * len(postfix)
TOP = -1

def isOperator(c):
    return True if c in ['^', '/', '+', '-', '*', '%'] else False


for index in range(len(postfix)):
    X = postfix[index]
    if X.isalnum():
        TOP, stack = sf.push(stack, TOP, X)
    
    if isOperator(X):
        TOP, op1, stack = sf.pop(stack, TOP)
        TOP, op2, stack = sf.pop(stack, TOP)
        string = f"({op2}{X}{op1})"
        TOP, stack = sf.push(stack, TOP, string)

print("Infix Equation: ",sf.pop(stack, TOP)[1])
import stack_functions as sf

prefix = input("Enter the prefix equation: ")

stack = [None]*len(prefix)
TOP = -1
i = len(prefix) - 1

def isOperator(c):
    return True if c in ['^', '/', '+', '-', '*', '%'] else False


while i >= 0:
    # sf.display_stack(stack, TOP)
    X = prefix[i]
    if X.isalnum():
        TOP, stack = sf.push(stack, TOP, X)
    if isOperator(X):
        TOP, op1, stack = sf.pop(stack, TOP)
        TOP, op2, stack = sf.pop(stack, TOP)
        string = f'{op1}{op2}{X}'
        TOP, stack = sf.push(stack, TOP, string)    
    i -= 1

print("\nPostFix equation: ", sf.pop(stack, TOP)[1])

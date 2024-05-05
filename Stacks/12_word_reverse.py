import stack_functions as sf

def create_stack(word):
    # print("[Create Stack]")
    stack = [None] * len(word)
    # print(stack, type(stack))
    TOP = -1
    # print(stack)
    for _letters in word:
        # print(_letters)
        TOP, stack = sf.push(stack, TOP, _letters)
    # sf.display_stack(stack, TOP)
    return stack, TOP
    

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
    word = input("Enter the string to reverse: ")
    output = ''
    for w in word.split():
        # print(f"\n### WORD : {w} ###")
        # create_stack(w)
        stack, TOP = create_stack(w)
        stack, TOP = reverseStack(stack, TOP)
        temp = ''.join(stack) + ' '
        output += temp
    print("Reversed String: ", output)




if __name__ == "__main__":
    main()
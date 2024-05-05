# Basic functions of array
# Functions to implement PUSH, POP, PEEK, PEEP, DELETE, SEARCH, DISPLAY, INSERT AT INDEX
'''
Parameters:
S: Stack
TOP: Pointer which keeps the index of top of stack
X: element 
'''

import stack_functions as sf
# Main program
S = [None] * 10  # Initialize stack with size 10
TOP = -1  # Initialize top pointer

choice = -1

while choice != 0:
    print("\n1. Push.\n2. Pop.\n3. Peek.\n4. Peep.\n5. Delete at index. \n6. Search. \
          \n7. Display. \n8. Size\n9. Insert at Index\n0. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1: # PUSH
        X = int(input("Enter the element to push onto the stack: "))
        TOP, S = sf.push(S, TOP, X)
    elif choice == 2: # POP
        TOP, popped_element, S = sf.pop(S, TOP)
        print(f"Element popped from stack: {popped_element}")
    elif choice == 3: # PEEK
        TOP, peek_element, S = sf.peek(S, TOP)
        print(f"Element at top of stack is: {peek_element}")
        print("Stack after Popping:\n", sf.display_stack(S, TOP))
    elif choice == 4: # PEEP
        index = int(input("Enter the index to peep at: "))
        TOP, peeped_element, S = sf.peep(S, TOP, index)
        print(f"Element at index {index} is {peeped_element}.")
    elif choice == 5: # DELETE AT INDEX
        index = int(input("\nEnter the index for deletion:"))
        TOP, S = sf.delete_at_index(S, TOP, index)
    elif choice == 6:
        element = int(input("Enter the element to search: "))
        list_of_indices = sf.search_element(S, TOP, element)
        indices_str = ', '.join(map(str, list_of_indices))
        output_str = f"The element {element} is at the indices {indices_str}"
        print(output_str)
    elif choice == 7: # DISPLAY
        sf.display_stack(S, TOP)
    elif choice == 8: # SIZE
        stack_size, elem_count = sf.size(S, TOP)
        print(f"Stack Size: {stack_size}\nElements in Stacks: {elem_count}")
    elif choice == 9: # INSERT AT INDEX
        index = int(input("Enter the index:"))
        element = int(input(f"Enter the element to insert at index {index}: "))
        TOP, S = sf.insert_at_index(S, TOP, index, element)      

print("Exiting program")


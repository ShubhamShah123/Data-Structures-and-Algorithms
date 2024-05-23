class StackHeap:
    def __init__(self, capacity) -> None:
        self.S = [None] * capacity
        self.TOP = -1
        self.capacity = capacity

    def _max_heapify(self, index):
        """
        Purpose: Make the heap property as MAX HEAP
        """  
        while index > 0:
            parent_index = (index - 1) // 2
            _, current_value = stack_peep(self.S, self.TOP, index)
            _, parent_value = stack_peep(self.S, self.TOP, parent_index)

            if current_value < parent_value:
                self.S[index], self.S[parent_index] = self.S[parent_index], self.S[index]
                index = parent_index
            else:
                break

    # end def

    def _min_heapify(self, index):
        """
        Purpose: Make the heap property as MIN HEAP
        """        
        size, _ = size(self.S, self.TOP)
        while index * 2 + 1 <= self.TOP:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if left <= self.TOP:
                _, left_value, _ = stack_peep(self.S, self.TOP, left)
                _, current_value, _ = stack_peep(self.S, self.TOP, smallest)
                if left_value < current_value:
                    smallest = left

            if right <= self.TOP:
                _, right_value, _ = stack_peep(self.S, self.TOP, right)
                _, current_value, _ = stack_peep(self.S, self.TOP, smallest)
                if right_value < current_value:
                    smallest = right

            if smallest != index:
                self.S[index], self.S[smallest] = self.S[smallest], self.S[index]
                index = smallest
            else:
                break
    # end def

    def push(self, value):
        """
        Purpose: 
        """
        if isStackFull(self.TOP, self.capacity):
            print("[HEAP IS FULL]")
            return
        self.S, self.TOP = push_to_stack(self.S, self.TOP, value)
        self._max_heapify(self.TOP)
        
    # end def
    def pop(self):
        """
        Purpose: Popping
        """
        if isStackEmpty(self.TOP):
            print("[HEAP IS EMPTY]")
            return None
        root = self.S[0]
        last_value = self.S[self.TOP]
        self.TOP, _, self.S = stack_pop(self.S, self.TOP)

        if not isStackEmpty(self.TOP):
            self.S[0] = last_value
            self._min_heapify(0)
        
        return root
        
    def peek(self):
        """
        Purpose: PEEKING AT THE TOP OF HEAP
        """
        return None if isStackEmpty(self.TOP) else self.S[0]
    
    def display(self):
        stack_display(self.S, self.TOP)
            
        
    # end def


def push_to_stack(S, TOP, X):
    if TOP >= len(S) - 1:
        print("Stack overflow!")
        return TOP, S
    
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

def stack_pop(S, TOP):
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

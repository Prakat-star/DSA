# Stack is a linear data structure that follows Last in First out Principle.
"""
Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
"""
# we use Lists to implement Stacks in python.

stack = []
# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))

# we can also make a dedicated stack class..
"""....."""
# Stack Implementation using Linked lists.
""" 
Linked List consists of nodes with some sort of data and a pointer to the next node..
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory
the nodes donot have to be stored contiguosly rifht after each other like elements stored in arrays.
Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.
"""

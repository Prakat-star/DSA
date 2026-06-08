"""
A Linked List is, as the word implies, a list where the nodes are linked
together. Each node contains data and a pointer. The way they are linked
together is that each node points to where in the memory the next node is placed.
"""

"""
Linked lists consist of nodes, and is a linear data structure we make ourselves,
unlike arrays which is an existing data structure in the programming language that we can use.

Nodes in a linked list store links to other nodes, but array elements do not
need to store links to other elements.

Linked lists are not allocated to a fixed size in memory like arrays are, so
linked lists do not require to move the whole list into a larger memory
space when the fixed memory space fills up, like arrays must.

"""

"""
Types of Linked Lists
There are three basic forms of linked lists:

Singly linked lists: one data and one address to next node
Doubly linked lists: one data and two address to previous and next node.
Circular linked lists: similar to single linked list but it also links last node to first node , where first node is called head and last is calle tail
(there is also doubly circular linked list)
"""

"""
Linked List Operations
Basic things we can do with linked lists are:

Traversal
Remove a node
Insert a node
Sort
"""

# Traversal of linked list : means to go thoruhg the linked list by following links from one node to next.
# typically done to search a specific node and real or modify the nodes context or to insert a node right before or after that node.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="->")
        currentNode=currentNode.next
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

# Using Linked List to find the Lowest Value in a Linked List.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(2)
node2 = Node(1)
node3 = Node(7)
node4 = Node(12)
node5 = Node(91)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))


# Deleating a node
def deleteSpecificNode(head,nodetoDelete):
    if head == nodetoDelete:
      return head.next
   
    currentNode = head
    while currentNode.next and currentNode.next != nodetoDelete:
      currentNode = currentNode.next
    
    if currentNode.next is None:
      return head
    
    currentNode.next = currentNode.next.next
    return head

print("Before deletion:")
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node4)
print("\nAfter deletion:")
traverseAndPrint(node1)

# insearting a node in a linked list:
def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)

# Time Complexity of Linked Lists Operations: O(n).


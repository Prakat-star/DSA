"""
A Binary Search Tree is a Binary Tree where every node's left child has a lower value, 
and every node's right child has a higher value.

A clear advantage with Binary Search Trees is that operations like search, delete, 
and insert are fast and done without having to shift values in memory.

A Binary Search Tree (BST) is a type of Binary Tree data structure,
to be any node "X in the tree it must have theese properties:
    The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.
    The right child, and all its descendants have higher values than X's value.
    Left and right subtrees must also be Binary Search Trees.

The size of a tree is the number of nodes in it (n).

"""

#Traversal of a Binary Search Tree:

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)

#Searching for a value in a BST:
"""
    Start at the root node.

    If this is the value we are looking for, return.

    If the value we are looking for is higher, continue searching in the right subtree.

    If the value we are looking for is lower, continue searching in the left subtree.

    If the subtree we want to search does not exist, depending on the programming language,
    return None, or NULL, or something similar, to indicate that the value is not inside the BST.

"""

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

# Search for a value
result = search(root, 13)
if result:
    print(f"\nFound the node with value: {result.data}.")
else:
    print("\nValue not found in the BST.")

# Time Complexity : o(h), where h is the height of the tree.

"""
INSERT A NODE IN A BST:
    Start at the root node.
    Compare each node:
    Is the value lower? Go left.
    Is the value higher? Go right.
    Continue to compare nodes with the new value until there is no right or left to compare with. That is where the new node is inserted.

    
inserting node this way means that the inserted node will always become a new leaf node.    
"""

def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
  return node

# Inserting new value into the BST
insert(root, 10)
inOrderTraversal(root)

"""
    FIND THE LOWESR VALUE IN A BST SUBTREE:
    Start at the root node of the subtree.
    Go left as far as possible.
    The node you end up in is the node with the lowest value in that BST subtree.

"""

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

# Find Lowest
print("\nLowest value:",minValueNode(root).data)

"""
DELETE A NODE IN A BST:
    If the node is a leaf node, remove it by removing the link to it.
    If the node only has one child node, connect the parent node of the node you want to remove to that child node.
    If the node has both right and left child nodes: Find the node's in-order successor, change values with that node, then delete it.

"""

def delete(node, data):
  if not node:
    return None

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    # Node with only one child or no child
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None
      return temp

    # Node with two children, get the in-order successor
    node.data = minValueNode(node.right).data
    node.right = delete(node.right, node.data)

  return node

# Delete node 15
delete(root,15)
inOrderTraversal(root)

"""
BST Compared to Other Data Structures
Data Structure	Searching for a value	Delete / Insert leads to shifting in memory
Sorted Array	    O(\log n)	                Yes
Linked List	        O(n)	                     No
Binary Search Tree	O(\log n)	                 No

"""


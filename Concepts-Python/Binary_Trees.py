"""
Binary Trees:
    A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, 
    a left child node and a right child node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:
    Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, 
    and run faster.
    Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
    Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
    Binary Trees can be represented as arrays, making the tree more memory efficient.
"""

# Binary Tree Implementation:
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.left.data:", root.right.left.data)

"""
Types of binary trees:
    A balanced Binary Tree has at most 1 in difference between its left and right subtree heights,
    for each node in the tree.

    A complete Binary Tree has all levels full of nodes, except the last level, 
    which is can also be full, or filled from left to right. The properties of a complete Binary Tree means
    it is also balanced.

    A full Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.

    A perfect Binary Tree has all leaf nodes on the same level,
    which means that all levels are full of nodes, and all internal nodes have two child nodes.
    The properties of a perfect Binary Tree means it is also full, balanced, and complete.
"""

"""
Binary Tree Traversal:
    Going through a Tree by visiting every node, one node at a time, is called traversal.
    
    There are two main categories of Tree traversal methods:

        Breadth First Search (BFS) is when the nodes on the same level are visited before going to the next level in the tree. 
        This means that the tree is explored in a more sideways direction.

        Depth First Search (DFS) is when the traversal moves down the tree all the way to the leaf nodes, 
        exploring the tree branch by branch in a downwards direction.

            There are three different types of DFS traversals:

            pre-order
            in-order
            post-order

"""

#Pre-order Traversal:one by visiting the root node first, then recursively do a pre-order traversal of the left subtree,
# followed by a recursive pre-order traversal of the right subtree.

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)



#In-order Traversal: does a recursive In-order Traversal of the left subtree, 
#visits the root node, and finally, does a recursive In-order Traversal of the right subtree.

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

#Post-order Traversal : works by recursively doing a Post-order Traversal of the left subtree and the right subtree,
#followed by a visit to the root node.

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


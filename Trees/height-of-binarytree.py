
# --------------------------------------------- Find height or depth of the binary tree ---------------------------------------------

# Given a binary tree, find height of it. Height of empty tree is 0.
# Recursively calculate height of left and right subtrees of a node and assign height to the node as max of the heights of two 
# children plus 1. 

class Node:
    def __init__(self, value, left = None, right = None) :
        self.value = value 
        self.left = left
        self.right = right
    
def height(root) :
    if root is None :
        return 0
    return 1 + max(height(root.left), height(root.right))

def main() :
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    print(f'height of the given tree is : {height(root)}')

if __name__ == '__main__' :
    main()

# $ python height-of-binarytree.py 
# height of the given tree is : 3

# T.C = O(n) on worst case scenario
# s.c = O(1)
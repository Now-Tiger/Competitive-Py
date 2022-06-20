#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-
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
    # root.right.left = Node(16)
    # root.right.right = Node(25)
    print(f'height of the given tree is : {height(root)}')

# T.C = O(n) on worst case scenario
# s.c = O(h) since we had to call stack, and h is the height of the tree.

# --------------------------------------------------------- Iterative Solution -------------------------------------------------------


from collections import deque as q

class Node :
    def __init__(self, value, left = None, right = None ) :
        self.value = value
        self.left, self.right = left, right


def height(node) :
    if node is None :
        return node 

    queue = q()
    queue.append(node)

    height = 0

    while queue :
        size = len(queue)
        while size > 0 :
            front = queue.popleft()

            if front.left :
                queue.append(front.left)
                
            if front.right :
                queue.append(front.right)
            size = size - 1 

        height = height + 1

    return height


if __name__ == '__main__' :
    r = Node(15)
    r.left = Node(10)
    r.right = Node(20)
    r.left.left = Node(8)
    # root.left.right = Node(12)
    # root.right.left = Node(16)
    # root.right.right = Node(25)
    main()      #       <- first solution
    print('-'*30)
    print(f'height of the given tree is : {height(r)}')

# $ pypy3 height-of-binarytree.py 
# height of the given tree is : 3
# ------------------------------ 
# height of the given tree is : 3

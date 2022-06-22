#!/usr/bin/ pyp3
# -*- coding: utf-8 -*-

# Program to calculate maximum depth of a binary tree.
# Below are two possible solutions:
#   1. Using recursion  
#   2. using queue data structure.


from __future__ import annotations
from typing import Optional

class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

class Solution(object):
    def max_depth_rec(self, root: Optional[Node]) -> int:
        """
            this is a recursive solution to calculate the 
            maximum depth of the tree. 
            function takes the root and starts visiting 
            every node from the root and at end compares 
            the maximum value and returns the value as the 
            maximum depth of the tree.
        """
        if not root:
            print('reached to the leaf !')
            return 0
        print(f'processing the node: {root.data}')
        # print(f'checking left node')
        leftnode = self.max_depth_rec(root.left) + 1
        # print(f'checking right node')
        rightnode = self.max_depth_rec(root.right) + 1
        # print(f'left depth: {leftnode} | right depth: {rightnode}')
        if leftnode > rightnode:
            return leftnode
        else: 
            return rightnode

if __name__ == "__main__":
    tree = Node(10)
    tree.left = Node(20)
    tree.right = Node(30)
    tree.left.left = Node(15)
    tree.left.left.left = Node(13)

    instance = Solution()
    depth = Solution.max_depth_rec(instance, tree)
    print(f"depth: {depth}")

    # depth_uncover = Solution.max_depth_rec(instance, tree.left)
    # print(f"depth: {depth_uncover}")

# $ pypy3 maximum-depth.py 
# processing the node: 10
# processing the node: 20
# processing the node: 15
# processing the node: 13
# reached to the leaf !  
# reached to the leaf !  
# reached to the leaf !  
# reached to the leaf !  
# processing the node: 30
# reached to the leaf !  
# reached to the leaf !  
# depth: 4
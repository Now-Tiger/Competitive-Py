#!/usr/bin/ pypy3

# --------------------------------- 543. Diameter of Binary Tree ------------------------------------
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1
# -------------------------------------------------------------------------------------------------

from __future__ import annotations
from collections import deque
from typing import Optional

class Node(object):
    '''
        Tree Node.
    '''
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None 

class Solution(object):
    def diameter(self, root: Optional[Node]) -> int:
        dia : int = 0
        """
         This is a naive solution using recursion.
         Therefore time complexity is O(n^2)
            - visiting every node (at least) twice.
         The space complexity is O(n) because of recursion. 
        """ 
        def dfs(self, root: Optional[Node]) -> None :
            nonlocal dia
            if not root :
                return 0
            lHeight = dfs(self, root.left)
            rHeight = dfs(self, root.right)
            dia = max(dia, lHeight + rHeight)
            return 1 + max(lHeight, rHeight)
        
        dfs(self, root)
        return dia

    def efficient_diameter(self, root: Optional[Node]) -> int:
        """
         The time complexity is O(n) because we are using 
         iterative approach.
         space complexity is o(n) where n is number of nodes
         present in the tree.
        """
        stack =  deque([root])
        depth = {None: 0}
        dia = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            leftDepth = depth.get(node.left, None)
            rightDepth = depth.get(node.right, None)
            if leftDepth == None or rightDepth == None:
                stack.append(node)
                stack.append(node.left)
                stack.append(node.right)
                continue
            dia = max(dia, leftDepth + rightDepth)
            depth[node] = 1 + max(leftDepth, rightDepth)
        return dia
        

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.left.left = Node(30)
    root.left.left.left = Node(40)
    root.right = Node(50)
    instance = Solution()
    diameter = Solution.diameter(instance, root)
    print(f'diameter: {diameter}')

    eff_dia = Solution.efficient_diameter(instance, root)
    print(f'diameter: {eff_dia}')

# $ pypy diameter-of-btree.py 
# diameter: 4   <== O(n^2)
# diameter: 4   <== O(n) 
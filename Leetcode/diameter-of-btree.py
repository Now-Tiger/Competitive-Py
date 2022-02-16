#!/usr/bin/ pypy3

# ----------------------------------- diameter of a binary tree -----------------------------------
#
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
#
# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Example 2:
# Input: root = [1,2]
# Output: 1
# ------------------------------------------------------------------------------------------------

from typing import Optional, List

class Node(object) :
    def __init__(self, data = None) -> None :
        self.data = data 
        self.left = None 
        self.right = None 

class Solution(object) :
    def diameter(self, root: Optional[Node]) -> int :
        dia : int = 0
        
        def dfs(root: Optional[Node]) -> None :
            nonlocal dia
            if not root :
                return 0
            lHeight = dfs(root.left)
            rHeight = dfs(root.right)
            dia = max(dia, lHeight + rHeight)
            return 1 + max(lHeight, rHeight)
        
        dfs(root)
        return dia 

if __name__ == "__main__" :
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    instance = Solution()
    print(Solution.diameter(instance, root))
    
# $ pypy diameter-opt.py 
# 3
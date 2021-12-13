#!/usr/bin/env pypy3

# ------------------------------------------- House Robber-III ------------------------------------------- 

# The thief has found himself a new place for his thievery again. There is only one entrance to this area, 
# called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized 
# that all houses in this place form a binary tree. It will automatically contact the police if two 
# directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting 
# the police.

# Example 1 : 
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# --------------------------------------------------------------------------------------------------------

from typing import List, Optional

class TreeNode(object) :
    def __init__(self, val: int) -> int :
        self.val = val
        self.left = None 
        self.right = None 

class Solution(object) :
    def rob(self, root: Optional[TreeNode]) -> int :
        
        def dfs(root: Optional[TreeNode]) -> int:
            if not root : 
                return [0, 0]

            left_pair = dfs(root.left)
            right_pair = dfs(root.right)

            with_Root = root.val + left_pair[1] + right_pair[1]
            without_Root = max(left_pair) + max(right_pair)

            return[with_Root, without_Root]
        return max(dfs(root))


if __name__ == '__main__' :
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    class_instance = Solution()
    res = Solution.rob(class_instance, root)
    print(res)

# $ pypy leetcode/house-robber-III.py 
# 7 
# T.C : O(n)
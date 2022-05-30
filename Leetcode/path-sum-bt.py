#!/usr/bin/ pypy3

# --------------------------------------- 112. Path Sum ---------------------------------------
# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1.
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2.
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3.
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
# --------------------------------------------------------------------------------------------

from __future__ import annotations
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None


class Solution(object):
    def hasPathSum(self, root: Optional[Node], target: int) -> bool:
        if target == None:
            return target
        if root == None:
            return False
        if (root.data == target and root.left is None and root.right is None):
            return True
        return (self.hasPathSum(root.left, target - root.data)
                or
                self.hasPathSum(root.right, target - root.data)
                )

    def hasSum_own(self, root: Optional[Node], target: int) -> bool:

        def leftsubsum(self, root: Optional[Node]) -> int:
            if root == None:
                return 0
            leftsum = root.data + leftsubsum(self, root.left)
            return leftsum

        def rightsubsum(self, root: Optional[Node]) -> int:
            if root == None:
                return 0
            rightsum = root.data + rightsubsum(self, root.right)
            return rightsum

        leftsum = leftsubsum(self, root)
        rightsum = rightsubsum(self, root)
        if root is None:
            return False
        elif leftsum == target or rightsum == target:
            return True
        return False


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.left.left = Node(20)
    root.right = Node(.30)
    instance = Solution()
    target: int = 50
    
    print(f'has sum: {Solution.hasPathSum(instance, root, target)} !')
    print(f'has sum: {Solution.hasPathSum(instance, root, 40)} !')
    print(f'has sum: {Solution.hasPathSum(instance, root, None)} !')
    print('-'*20)
    print(f'has sum: {Solution.hasSum_own(instance, root, 0)} !')

# $ pypy3 path-sum-bt.py 
# has sum: True !
# has sum: False !    
# has sum: None !     
# --------------------
# has sum: False !    

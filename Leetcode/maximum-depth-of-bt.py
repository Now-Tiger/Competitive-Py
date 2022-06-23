#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-
# -------------------------------------------------------- Maximum Depth of Binary Tree --------------------------------------------------------
#
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,null,2]
# Output: 2
# ----------------------------------------------------------------------------------------------------------------------------------------------

from __future__ import annotations
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int):
        self.left = self.right = None
        self.val = val


class Solution:
    def max_depth(self, root: Optional[Node]) -> int:
        """
            efficient approach an alternative to recursive
            approach but takes space(queue) to store nodes. 
        """
        depth: int = 0
        queue = deque([root])
        if not root:
            print('reached leaf')
            return 0
        while queue:
            size: int = len(queue)
            for i in range(size):
                root = queue.popleft()
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
            depth += 1
        return depth

    def maxDepth(self, root: Optional[Node]) -> int:
        """
            recursive approach.
        """
        if root is None:
            return 0
        return (max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1)


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)

    #           15
    #         /    \
    #        10    20
    #      /   \
    #     8    12

    instance = Solution()
    res_first = Solution.max_depth(instance, root)
    res_second = Solution.maxDepth(instance, root.right)   # root.right is 20
    print(f"iterative approach: {res_first}")
    print(f"recursive approach: {res_second}")

# $ pypy maximum-depth-of-bt.py
# iterative approach: 3
# recursive approach: 1

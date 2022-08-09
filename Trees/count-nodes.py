#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Problem statement: Count Number of Nodes in a Binary Tree (complete binary tree is given)
# -----------------------------------------------------------------------------------------
# Below I've given two(methods) solutions for the problem.

import time
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None


class Solution(object):
    def left_height(self, root: Optional[Node]) -> int:
        height: int = 0
        if not root:
            return 0
        while (root != None):
            height += 1
            root = root.left
        return height

    def right_height(self, root: Optional[Node]) -> int:
        height: int = 0
        if not root:
            return 0
        while (root != None):
            height += 1
            root = root.right
        return height

    def count_nodes(self, root: Optional[Node]) -> int:
        """
            Time Complexity: O(log^2 N)
                - Reason: To find the leftHeight 
                  and right Height we need only logN 
                  time and in the worst case we will 
                  encounter the second 
                  case(leftHeight!=rightHeight) for at 
                  max logN times, so total time 
                  complexity will be O(log N * logN)

            Space Complexity: O(logN)
                - Reason: Space is needed for the 
                  recursion stack when calculating 
                  height. As it is a complete tree, 
                  the height will always be logN.
        """
        if not root:
            return 0
        leftheight: int = self.left_height(root)
        rightheight: int = self.right_height(root)
        if (leftheight == rightheight):
            return (1 << leftheight) - 1
        leftnodes: int = self.count_nodes(root.left)
        rightnodes: int = self.count_nodes(root.right)
        return 1 + leftnodes + rightnodes

    def count_nodes_recursive(self, root: Optional[Node]) -> int:
        """
            Time Complexity: O(N).
                - reason: traversing every nodes of the tree
            Space Complexity: O(logN)
                - reason: space is needed for the recursion stack.
                - As it is a complete tree, the height of that 
                  stack will always be logN.
        """
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + \
                   self.count_nodes(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    root.left.left.left = Node(80)
    root.left.left.right = Node(90)
    root.left.right.left = Node(100)
    root.left.right.right = Node(101)

    instance = Solution()
    total_nodes = Solution.count_nodes(instance, root)
    print(f"total nodes: {total_nodes}")

    print(f"total nodes: {Solution.count_nodes_recursive(instance, root)}")

# $ pypy3 count-nodes.py
# total nodes: 11
# total nodes: 11

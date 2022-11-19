#!/usr/bin/ pyp3
# -*- coding: utf-8 -*-

# Program to calculate maximum depth of a binary tree.
# Below are two possible solutions:
#   1. using queue data structure.
#   2. Using recursion

from __future__ import annotations
from collections import deque
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class Solution(object):
    def max_depth(self, root: Optional[Node]) -> int:
        """
            type root: Node
            return type: int
        """
        depth: int = 0
        if not root:
            print('reached leaf')
            return depth

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                root = queue.popleft()
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
            depth += 1
        return depth

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
        leftdepth = self.max_depth_rec(root.left) + 1
        rightdepth = self.max_depth_rec(root.right) + 1
        return max(leftdepth, rightdepth)


def main() -> None:
    tree = Node(10)
    tree.left = Node(20)
    tree.right = Node(30)
    tree.left.left = Node(15)
    tree.left.left.left = Node(13)

    instance = Solution()
    depth_q = Solution.max_depth(instance, tree)
    print(f"depth: {depth_q}")

    print('-' * 20)

    depth_rec = Solution.max_depth_rec(instance, tree.left)
    print(f"depth: {depth_rec}")
    
if __name__ == "__main__":
    main()

# $ pypy3 maximum-depth.py
# depth: 4
# --------------------
# processing the node: 20
# processing the node: 15
# processing the node: 13
# reached to the leaf !
# reached to the leaf !
# reached to the leaf !
# reached to the leaf !
# depth: 3

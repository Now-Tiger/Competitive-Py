#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None


class Solution(object):
    def minimum_depth_(self, root: Optional[Node]) -> int:
        """
            good to have consideration of edge cases 
            in the program. 
        """
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.minimum_depth_(root.right) + 1
        # elif root.right is None:
        else:
            self.minimum_depth_(root.left) + 1
        return min(self.minimum_depth_(root.left), self.minimum_depth_(root.right)) + 1

    def min_depth(self, root: Optional[Node]) -> int:
        """
            naive implementation.
            T.C: O(n) since function has to visit very node. 
        """
        if root == None:
            return 0
        return 1 + min(self.min_depth(root.left), self.min_depth(root.right))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    instance = Solution()

    print(Solution.minimum_depth_(instance, root))
    print(Solution.min_depth(instance, root))

# $ pypy3 minimum-depth.py 
# 2
# 2
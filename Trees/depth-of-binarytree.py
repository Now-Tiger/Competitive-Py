#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

from __future__ import annotations 
from typing import Optional

class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data 
        self.left = self.right = None 

class Solution(object):
    """
        function can find depth of the tree from a node.
    """
    def find_depth(self, root: Optional[Node], value: int) -> int:
        distance: int = -1
        if root == None:
            return -1
        elif root.data == value:
            return distance + 1
        distance = self.find_depth(root.left, value)
        if distance >= 0:
            return distance + 1
        distance = self.find_depth(root.right, value)
        if distance >= 0:
            return distance + 1
        return distance 


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(15)
    root.left.left = Node(20)
    root.left.right = Node(25)
    root.left.right.right = Node(45)
    root.right.left = Node(30)
    root.right.right = Node(35)
    instance = Solution()

    #            5
    #       10      15
    #    20   25   30  32
    #           45
  
    node_value: int = 45
    print(Solution.find_depth(instance, root, node_value))

    node_value: int = 15
    print(Solution.find_depth(instance, root, node_value))

# $ pypy3 depth-of-binarytree.py 
# 3
# 1

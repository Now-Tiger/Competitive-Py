#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Given a sorted array, give an algorithm to build BST (Binary search tree) from that array.

from __future__ import annotations
from typing import Optional


class Node(object):
    def __init__(self, data: Optional[int]) -> None:
        self.data = data
        self.left = None
        self.right = None


class Solution(object):
    def build_bst(self, A: list) -> Node:
        left: int = 0
        right: int = len(A) - 1
        if left > right:
            return None
        new_node = Node(None)
        if not new_node:
            print("Memory Error")
            return
        elif left == right:
            new_node.data = A[left]
            new_node.left = None
            new_node.right = None
        else:
            mid: int = left + (right - left) // 2
            new_node.data = A[mid]
            new_node.left = self.build_bst(A[:mid])
            new_node.right = self.build_bst(A[mid + 1:])
        return new_node

    def printtree(self, root: Node) -> str:
        """
            this function returns the inorder
            traversal of the BST.
            --------------------------------
            Inorder traversal of an bst always 
            gives sorted elements at the output.
        """
        if root.left:
            self.printtree(root.left)
        print(root.data, end=", ")
        if root.right:
            self.printtree(root.right)

    def preorder(self, root: Node) -> str:
        if not root:
            return 0
        print(root.data, end=", ")
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7]
    instance = Solution()
    root = Solution.build_bst(instance, A)
    Solution.printtree(instance, root)
    # Solution.preorder(instance, root)

# $ pypy3 Trees/array-to-bst.py
# 1, 2, 3, 4, 5, 6, 7,

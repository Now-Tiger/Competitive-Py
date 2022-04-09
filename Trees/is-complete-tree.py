#!/usr/bin/ pypy3

from __future__ import annotations
from typing import Optional, List


class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Solution(object):
    def count_nodes(self, root: Node) -> int:
        if root is None:
            return 0
        return (1 + self.count_nodes(root.left) + self.count_nodes(root.right))

    def is_complete_bt(self, root: Node, index: int, total_nodes: int) -> bool:
        if root is None:
            return True
        elif index >= total_nodes:
            return False
        return (self.is_complete_bt(root.left, 2 * index + 1, total_nodes)
                and
                self.is_complete_bt(root.right, 2 * index + 2, total_nodes))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    instance = Solution()
    nodes = Solution.count_nodes(instance, root)
    print(f"total nodes in this tree are: {nodes}")

    index = 0

    if Solution.is_complete_bt(instance, root, index, nodes):
        print("Tree is complete tree !")
    else:
        print("Tree is not a complete tree")

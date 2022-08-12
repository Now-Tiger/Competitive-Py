#!/usr/bin/ pypy3

# Problem Statement: Check whether the given Binary Tree is a Balanced Binary Tree or not. 
# A binary tree is balanced if, for all nodes in the tree, the difference between left and right 
# subtree height is not more than 1.

from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None


class Solution(object):
    def is_balanced_tree(self, root: Optional[Node]) -> bool:
        """
            Time Complexity: O(N) 
            ------------------------
            Space Complexity: O(1) Extra Space + O(H) 
            Recursion Stack space (H = height of tree) 
        """
        return self.dfs(root) != -1

    def dfs(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        leftheight: int = self.dfs(root.left)
        rightheight: int = self.dfs(root.right)
        if (leftheight == -1):
            return -1
        elif (rightheight == -1):
            return -1
        elif abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.right = Node(60)
    root.right.left = Node(70)
    instance = Solution()
    print(Solution.is_balanced_tree(instance, root))

# $ pypy3 Trees/is-balanced-binarytree.py
# True

#!/usr/bin/ pypy3

# ----------------- Give an algorithm for finding sum of all the elements of binary tree ------------

from typing import List, Optional

class Node(object):
    def __init__(self, data = None) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

class Solution(object):
    def find_sum(self, root: Optional[Node]) -> int:
        if root == None:
            return 0
        return root.data + self.find_sum(root.left) + self.find_sum(root.right)

if __name__ == "__main__":

    tree = Node(3)
    tree.left = Node(3)
    tree.right = Node(5)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.right.left = Node(8)

    instance = Solution()
    res = Solution.find_sum(instance, tree)
    print(res)


# $ pypy sum-of-all-elements.py 
# 26
# Time complexity: O(n) | Space compexity: O(n)
#!/usr/bin/env python3

# 404. 
# ------------------------------------------- Sum of Left Leaves -------------------------------------------
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# Example 1 :
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
#
# Example 2:
# Input: root = [1]
# Output: 0
#
# ----------------------------------------------------------------------------------------------------------

from typing import Optional, List
from collections import deque 

class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None 

class Solution(object) :
    def sumofLeftLeaves(self, root : Optional[Node]) -> int:
        if root == None :
            return 0
        q = deque([root])
        res = 0

        while q :
            node = q.popleft()

            if node.left :
                q.append(node.left)
                if not node.left.left and not node.left.right :
                    res += node.left.val
            if node.right :
                q.append(node.right)

        return res

if __name__ == '__main__' :
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    root.right.left = Node(5)

    #           1
    #         /   \
    #        2     4
    #       /     /
    #      3     5

    instance = Solution()
    print(Solution.sumofLeftLeaves(instance, root))


# --------------------------------------------------------------------------------------------------------
class Solution :
    def sumLeftLeaves(self, root) :
        if root == None :
            return 0
        elif root.left != None and root.left.left == None and root.left.right == None :
            return root.left.val + self.sumLeftLeaves(root.right)
        return self.sumLeftLeaves(root.left) + self.sumLeftLeaves(root.right)   

if __name__ == '__main__' :
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    root.right.left = Node(9)

    #           1
    #         /   \
    #        2     4
    #       /     /
    #      3     9

    instance = Solution()
    print(Solution.sumLeftLeaves(instance, root))


# $ python Trees/sum-of-left-leaves.py
# 8
# 12
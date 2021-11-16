#!/usr/bin/env python3

# ------------------------------------ Inorder Traversal in generic tree ------------------------------------

from typing import List 
class Node(object) :
    def __init__(self, n, val = None) :
        self.children = [None] * n
        self.val = val

class Solution :
    def inorder(self, node : 'Node') -> List[int] :
        if node == None :
            return 
        total = len(node.children)
        for i in range(total - 1) :
            self.inorder(node.children[i])
        # print current node's data/value 
        self.inorder(node.children[total - 1])
        print(node.val, end = ' ')

if __name__ == '__main__' :
    n = 3
    root = Node(n, 1)
    root.children[0] = Node(n, 2)
    root.children[1] = Node(n, 3)
    root.children[2] = Node(n, 4)

    root.children[0].children[0] = Node(n, 5) 
    root.children[0].children[1] = Node(n, 6)
    root.children[0].children[2] = Node(n, 7)

    # Create the following tree 
        #          1
        #       /  |  \
        #      2   3   4
        #    / | \
        #   5  6  7

    instance = Solution()
    Solution.inorder(instance, root)

# $ python Trees/generictree-inorder.py
# 5 6 7 2 3 4 1 
    
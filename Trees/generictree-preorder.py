#!/usr/bin/env python3

# ---------------------- preorder traversal in generic tree -------------------------------

from collections import deque
from typing import List

class Node(object) :
    def __init__(self, val = None, ) :
        self.val = val
        self.children = []

class Solution :
    def preorder(self, root : 'Node') -> List[int] :
        stack = deque([])
        # preorder contains all the visited nodes
        preorder = []
        preorder.append(root.val)
        stack.append(root)
        while len(stack) > 0 :
            # Flag to check to whether all nodes are beign visited.
            flag = 0
            
            # CASE 1- If Top of the stack is a leaf
            # node then remove it from the stack :
            if len((stack[len(stack) - 1]).children) == 0 :
                X = stack.pop()
                
                # CASE 1- If Top of the stack is a leaf
                # node then remove it from the stack:
            else :
                par = stack[len(stack) - 1]
            
            for i in range(0, len(par.children)) :
                if par.children[i].val not in preorder :
                    flag = 1
                    stack.append(par.children[i])
                    preorder.append(par.children[i].val)
                    break; 
            if flag == 0 :
                stack.pop()
        print(preorder)
 

if __name__ == '__main__' :
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children.append(Node(4)) 
    root.children[0].children.append(Node(5)) 
    root.children[0].children[0].children.append(Node(10)) 
    root.children[0].children.append(Node(6)) 
    root.children[0].children[1].children.append(Node(11))
    root.children[0].children[1].children.append(Node(12))
    root.children[0].children[1].children.append(Node(13)) 
    root.children[2].children.append(Node(7))
    root.children[2].children.append(Node(8))
    root.children[2].children.append(Node(9))

    #              1
    #           /  |  \
    #          /   |   \
    #         2    3    4
    #        / \      / | \
    #       /   \    7  8  9
    #      5     6    
    #     /    / | \ 
    #    10   11 12 13

    instance = Solution()
    Solution.preorder(instance, root)

# $ python Trees/n-ary-preorder.py 
# [1, 2, 5, 10, 6, 11, 12, 13, 3, 4, 7, 8, 9]

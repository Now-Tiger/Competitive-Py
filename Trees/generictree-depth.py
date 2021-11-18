#!/usr/bin/env python3
# ----------------------
# problem : You have given an array P, where p[i] indicates parent of ith node in the tree. 
#           (assume that the root node is indicated with -1) 
#           Give an algorithm to find the height or depth of the tree :
#
# 
# Ex : The array P is given :  | -1 | 0 | 1 | 6 | 6 | 0 | 0 | 2 | 7 |
#                                 0   1   2   3   4   5   6   7   8          
#
# 
# Array P indicates the parent of the nodes written exactly down below them
# The root index is shown by -1
# Parent of node 1 is 0 also node 5 and node 6 has parent node 0; this mean that one parent has 3 children,
# Thus this Tree is Generic Tree 

# ------ Naive Approach ------ 
from typing import List

def findDepht(P : List[int]) -> List[int] :
    maxDepth = -1
    currDepth = -1 
    for i in range(0, len(P)) :
        currDepth = 0
        j = i
        while (P[j] != -1) :
            currDepth += 1
            j = P[j]
            if (currDepth > maxDepth) :
                maxDepth = currDepth
    return maxDepth 

print(findDepht(P = [-1, 0, 1, 6, 6, 0, 0, 2, 7]))

# $ python generictree-depth.py 
# 4

# Time complexity : O(n^2)          Space complexity : O(1)

# We can improve t.c; we can use hashtable to store previously calculated nodes but space complexity 
# increases.
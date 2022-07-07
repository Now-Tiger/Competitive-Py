
# ------------------------------------------------ Cousins in Binary Tree ------------------------------------------------
# 
#               In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.
# 
# Example 1:
#           
#           1
#         /   \
#        2     3
#       /       
#      4
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
#
# Example 2:
#
#           1
#         /   \
#        2     3
#         \     \
#          4     5  
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
# ------------------------------------------------------------------------------------------------------------------------

from typing import Optional
from collections import deque


class TreeNode :
    def __init__(self, val = 0) :
        self.val = val 
        self.left = None
        self.right = None

class Solution :
    def cousins_naive(self, root: Optional[Node]) -> bool:
        """
            This is a naive recursive solution.
            we have been told that, 'Two nodes of a binary 
            tree are cousins if they have the same depth, 
            but have different parents.'
            Therefore in this solution we can just check 
            left and right depths from root.
            -----------------------------------------------
            This is not a correct solution. below solution
            is better one.
        """
        if not root: return 0
        left_depth: int = self.cousins_naive(root.left) + 1
        right_depth: int = self.cousins_naive(root.right) + 1
        return left_depth == right_depth
        
        
    def cousins(self, root, x, y) :
        queue = deque()
        queue.append((root, 0))
        dist = {}
        while queue :
            node, depth = queue.popleft()
            if node.left :
                dist[node.left.val] = (node.val, depth + 1)
                queue.append((node.left, depth + 1))
            if node.right :
                dist[node.right.val] = (node.val, depth + 1)
                queue.append((node.right, depth + 1))
        if x not in dist or y not in dist :
            return False
        x_parent, x_depth = dist[x]
        y_parent, y_depth = dist[y]
        return x_depth == y_depth and x_parent != y_parent


if __name__ == '__main__' :

    # Example 1 : [1,2,3,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    class_instance = Solution()
    res = Solution.cousins(class_instance, root, 4, 3)
    print(res)

# $ python cousins-in-binarytree.py 
# False

# Time Complexity : We traversal all elements of tree once so total time complexity is O(n) 
#                   where n is number of the tree nodes.


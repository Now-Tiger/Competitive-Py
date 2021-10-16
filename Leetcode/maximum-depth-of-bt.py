
# -------------------------------------------------------- Maximum Depth of Binary Tree --------------------------------------------------------
#
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. 
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,null,2]
# Output: 2
# ----------------------------------------------------------------------------------------------------------------------------------------------

class Node :
    def __init__(self, val) :
        self.left = self.right = None
        self.val = val
    
class Solution :
    def maxDepth(self, root) :
        if root is None :
            return 0
        return (max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1)


if __name__ == '__main__' :
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)

    #           15
    #         /    \
    #        10    20
    #      /   \    
    #     8    12

    class_instance = Solution()
    res = Solution.maxDepth(class_instance, root.right)   # root.right is 20
    print(res)

# $ python maximum-depth-of-bt.py 
# 1
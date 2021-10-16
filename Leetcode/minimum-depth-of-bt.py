
# ------------------------------------------------ Minimum Depth of Binary Tree ------------------------------------------------
# 
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# ------------------------------------------------------------------------------------------------------------------------------

class Node(object) :
    def __init__(self, val) :
        self.val = val 
        self.left = None
        self.right = None


class Solution :
    def minDepth(self, root) :
        if root is None :
            return 0
        if root.left and root.right :
            return min(self.minDepth(root.left), self.minDepth(root.right)) +1
        else :
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__' :
    # [3, 9, 20, null, null, 15, 7]
    Tree = Node(3)
    Tree.left = Node(9)
    Tree.right = Node(20)
    # if left subnode of root has null values; 
    # Then we better leave that side as empty.
    Tree.right.left = Node(15)
    Tree.right.left = Node(7)

    class_instance = Solution()
    res = Solution.minDepth(class_instance, Tree)
    print(f'Height of first tree : {res}')

    print(f'\n----- example 2 -----\n')
   
   
    # [2, null, 3, null, 4, null, 5, null, 6]
    #
    #                   2
    #                /     \
    #             null      3
    #                     /   \
    #                  null    4
    #                        /   \
    #                     null    5
    #                           /   \
    #                          null  6

    root = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    root.right.right.right.right = Node(6)

    class_instance = Solution()
    res = Solution.minDepth(class_instance, root)
    print(f'Height of second tree : {res}')


# $ python minimum-depth-of-bt.py 
# Height of first tree : 2

# ----- example 2 -----    

# Height of second tree : 5

# Time complexity : O(n)
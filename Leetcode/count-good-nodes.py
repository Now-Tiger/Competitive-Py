
# 1448. 
# ------------------------------------------------ Count Good Nodes in Binary Tree ------------------------------------------------
# 
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value 
# greater than X.
# Return the number of good nodes in the binary tree.
#
# Example 1 :
# Input: root = [3, 1, 4, 3, null, 1, 5]
# Output: 4
# 
# Example 2 :
# Input: root = [3, 3, null, 4, 2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
#
# ---------------------------------------------------------------------------------------------------------------------------------

class Node(object) :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None
    
class Solution :
    def goodNodes(self, root) :
        def dfs(root, curr_max) :
            if not root :
                return 0 
            curr_max = max(curr_max, root.val)
            res = int(curr_max <= root.val) + \
                    dfs(root.left, curr_max) + \
                    dfs(root.right, curr_max)
            return res 
        return dfs(root, root.val)


if __name__ == '__main__' :
    # [3, 3, null, 4, 2]
    root = Node(3)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)
    print(f'Good Nodes : {Solution.goodNodes(Solution, root)}')


# $ python count-good-nodes.py 
# Good Nodes : 3

# Time :  O(n)
# Space : O(h)

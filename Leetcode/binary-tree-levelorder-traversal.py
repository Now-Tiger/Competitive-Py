# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []

        levels = []
        seq = collections.deque()
        seq.append(root)

        # while job exist :
        while seq :
            nos = len(seq)
            buff = []

            for _ in range(nos) :
                node = seq.popleft()
                buff.append(node.val)
                if node.left : 
                    seq.append(node.left)
                if node.right :
                    seq.append(node.right)
            levels.append(buff)
        
        return levels




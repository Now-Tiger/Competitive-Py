## Right Side View of Binary Tree.
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

__Example 1__ :<br>
__Input :__ root = [1,  2,  3,  null,  5,  null,  4]<br>
__Output :__ [1, 3, 4]


__Example 2__ :<br>
__Input :__ root = [1, null, 3]<br>
__Output :__ [1, 3]

``` python
class Node(object) :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

class Solution :
    def rightView(self, root) :
        def dfs(root, res, lvl) :
            if not root :
                return 
            if root and lvl == len(res) :
                res.append(root.val)
            dfs(root.right, res, lvl + 1)
            dfs(root.left, res, lvl + 1)
            return res
        return dfs(root, [], 0)

def main() :
    # example 1 : [1, 2, 3, null, 5, null, 4]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(4)

    instance = Solution()
    res = Solution.rightView(instance, root)
    print(f'Right view of tree 1. : {res}')

    # example 2 : [1,null,3]
    node = Node(1)
    node.right = Node(3)
    print(f'Right view of tree 2. : {Solution.rightView(Solution, node)}')

if __name__ == '__main__' :
    main()

# $ python binary-tree-right-view.py
# Right view of tree 1. : [1, 3, 4]
# Right view of tree 2. : [1, 3]

# Time complexity : O(n)

```

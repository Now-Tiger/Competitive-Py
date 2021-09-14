# 617
# -----------------------------------------  Merge Two Binary Trees -----------------------------------------

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while 
# the others are not. You need to merge the two trees into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = self.right = None

def inorder(node) :
    if not node : return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

# Function to merge two binary trees 
def mergeTrees(tree1, tree2) :
    if not tree1 : 
        return tree2
    if not tree2 : 
        return tree1
    tree1.data += tree2.data
    tree1.left = mergeTrees(tree1.left, tree2.left)
    tree1.right = mergeTrees(tree1.right, tree2.right)
    return tree1

def main() :
    # Let us construct the first Binary Tree
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    #
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)
    tree1.left.right = Node(5)
    tree1.right.right = Node(6)

    # Let us construct the second Binary Tree
    #       4
    #     /   \
    #    1     7
    #   /     /  \
    #  3     2    6   
    tree2 = Node(4)
    tree2.left = Node(1)
    tree2.right = Node(7)
    tree2.left.left = Node(3)
    tree2.right.left = Node(2)
    tree2.right.right = Node(6)

    tree3 = mergeTrees(tree1, tree2)
    inorder(tree3)


# Driver code :
if __name__ == '__main__' :
    print('Two binary trees mergred into one printed in inorder fashion :')
    #       5
    #     /   \
    #    3     10
    #   /  \   /  \
    #  7    5 2    12   
    main()


# $ python merge-two-binarytrees.py 
# Two binary trees mergred into one printed in inorder fashion :
# 7 3 5 5 2 10 12 

# T.C = O(n)    S.C = O(n)



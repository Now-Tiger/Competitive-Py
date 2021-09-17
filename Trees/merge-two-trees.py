# 617
# -----------------------------------------  Merge Two Binary Trees -----------------------------------------

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while 
# the others are not. You need to merge the two trees into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

from queue import Queue

class Node :
    def __init__(self, value) :
        self.value = value
        self.left = self.right = None

    def levelorder(root) :
        if root is None : return
        q = Queue()
        q.put(root)
        while not q.empty() :
            node = q.get()
            if node == None :
                continue
            print(node.value)
            q.put(node.left)
            q.put(node.right)


def mergetrees(tree1, tree2) :
    if not tree1 :
        return tree2
    if not tree2 : 
        return tree1
    tree1.value += tree2.value 
    tree1.left = mergetrees(tree1.left, tree2.left)
    tree1.right = mergetrees(tree1.right, tree2.right)
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


    tree3 = mergetrees(tree1, tree2)
    #       5
    #     /   \
    #    3     10
    #   /  \   /  \
    #  7    5 2    12 
    tree3.levelorder()


if __name__ == '__main__' :
    print('Two binary trees mergred into one printed in levelorder fashion :')
    main()

# $ python mergeTree.py 
# Two binary trees mergred into one printed in levelorder fashion : 
# 5
# 3 
# 10
# 7 
# 5 
# 2 
# 12


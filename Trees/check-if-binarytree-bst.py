
# ---------------------------- Check if binary tree is BST or Not ----------------------------

class Node(object) :
    def __init__(self, value) :
        self.value = value 
        self.left = None
        self.right = None

# Return true if given tree is BST.
def isBST(root, l = None, r = None) :
    if root == None : 
        return True
        
    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (l != None and root.value <= l.value) : 
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if r != None and root.value >= r.value : 
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and isBST(root.right, root, r)


if __name__ == '__main__' :
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    root.right.left.left = Node(40)
    if isBST(root, None, None) :
        print("Is BST")
    else :
        print("Not a BST")


# $ python check-if-binarytree-bst.py
# Not a BST

# Time Complexity: O(n) 
# Auxiliary Space: O(1) if Function Call Stack size is not considered, otherwise O(n)



# Inorder Traversal in a tree.

class Node(object) :
    def __init__ (self, value) :
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_val) :
        if self.value :
            if new_val < self.value :
                if self.left is None : 
                    self.left = Node(new_val)
                else :
                    self.left.insert(new_val)
            elif new_val > self.value :
                if self.right is None :
                    self.right = Node(new_val)
                else :
                    self.right.insert(new_val)
        else :
            self.value = new_val

    def printTree(self) :
        if self.left :
            self.left.printTree()
        print(self.value),
        if self.right :
            self.right.printTree()
    
    def inorder(self, root) :
        res = []
        if root :
            res = self.inorder(root.left)
            res.append(root.value)
            res = res + self.inorder(root.right)
        return res 
    
tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
print(tree.printTree()) 
print(tree.inorder(tree))


# How above tree would look :
#
#               27          * since it's node/root/parent of our tree.
#            /      \
#          14        35
#         /  \      /  \  
#        10  19    31   42

# Steps Inorder Traversal follows : [Left, root, right] <-- 
#                                   Technique which I keep in mind.

# o/p : [10, 14, 19, 27, 31, 35, 42]





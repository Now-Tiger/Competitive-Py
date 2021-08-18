
# preorder traversal in a tree data structure

class Node(object) :
    def __init__(self, value) :
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
        print(self.value)
        if self.right :
            self.right.printTree()

    def preorder(self, root) :
        # root, left, right
        res = []
        if root :
            res.append(root.value)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

# Driver code :    
tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
tree.printTree()
print('-'*30)
print('Preorder traversal : {}'.format(tree.preorder(tree)))

# How above tree would look :
#
#               27          * since it's node/root/parent of our tree.
#            /      \
#          14        35
#         /  \      /  \  
#        10  19    31   42

# Steps pre-order Traversal follows : [Root, left, right] <-- 
#                                     Technique which I keep in mind.

# o/p : [27, 14, 10, 19, 35, 31, 42]

#!/usr/bin/env python3
# Level order traversal in Binary tree :

from queue import Queue 

class Node(object) :
    def __init__(self, value) :
        self.value = value
        self.left = None 
        self.right = None

    def insert(root, new_val) :
        if root.value :
            if new_val < root.value :
                if root.left is None : root.left  = Node(new_val)
                else :
                    root.left.insert(new_val)
            elif new_val > root.value :
                if root.right is None : root.right = Node(new_val)
                else :
                    root.right.insert(new_val)
        else :
            root.value = new_val

    
    def levelorder(root) :
        if root is None : return
        q = Queue()
        q.put(root)
        while not q.empty() :
            node = q.get()
            if node == None : continue
            print(node.value)
            q.put(node.left)
            q.put(node.right)

    def printtree(self) :
        if self.left :
            self.left.printtree()
        print(self.value),
        if self.right :
            self.right.printtree()

tree = Node(15)
tree.insert(10)
tree.insert(25)
tree.insert(6)
tree.insert(14)
tree.insert(20)
tree.insert(60)

#tree.printtree()
print('Level order traversal:\n------------')
tree.levelorder()

# How above tree would look :
#
#               15              * since it's node/root/parent of our tree.
#            /      \
#          10        25
#         /  \      /  \  
#        6   14   20    60

# o/p : 15
#       10
#       25
#       6 
#       14
#       20
#       60

# T.C = O(n)



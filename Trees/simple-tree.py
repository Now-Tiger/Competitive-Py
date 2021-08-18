
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

    def printtree(self) :
        if self.left :
            self.left.printtree()
        print(self.value)
        if self.right :
            self.right.printtree()

tree = Node(12)
tree.insert(6)
tree.insert(14)
tree.insert(3)
tree.printtree()

# o/p : 3
#       6 
#       12
#       14


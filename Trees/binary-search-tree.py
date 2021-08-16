
# Implement a binary search tree. 
# Insert elements.
# Search one which iss insearted : return True.
# Search one which is not in the tree : return False.

class Node(object) :
    def __init__(self, value) :
        self.value = value      # node data 
        self.left = None        # left child
        self.right = None       # right child

class BST(object) :
    def __init__(self, root) :
        self.root = Node(root) 

    def insert(self, new_val) :
        self.insert_helper(self.root, new_val) 
    
    def insert_helper(self, current, new_val) :
        if current.value < new_val :
            if current.right :
                self.insert_helper(current.right, new_val)
            else :
                current.right = Node(new_val) 
        else :
            if current.left :
                self.insert_helper(current.left, new_val) 
            else :
                current.left = Node(new_val)

    def search(self, find_val) :
        return self.search_helper(self.root, find_val) 
    
    def search_helper(self, current, find_val) :
        if current :
            if current.value == find_val :
                return True
            elif current.value < find_val :
                return self.search_helper(current.right, find_val) 
            else :
                return self.search_helper(current.left, find_val) 
        return False 


# Setting up Tree :)
tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.search(4))
print('-'*20)
print(tree.search(6))



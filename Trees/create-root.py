


class Node(object) :
    def __init__(self, value) :
        self.value = value      # Node data
        self.right = None
        self.left = None

    def print_tree(self) :
        print(self.value)

root = Node(10)
root.print_tree()






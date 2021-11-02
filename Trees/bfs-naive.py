#!/usr/bin/env python3

# -------------------------------------- Depth first search class implementation : -------------------------------------------

class Node :
    def __init__(self, value) :
        self.value = value 
        self.children = []
    
    def __repr__(self) -> str:
        return f"{self.value}"
    
    def addChild(self, node) :
        self.children.append(node)

    def __iter__(self) :
        return iter(self.children)

    def depthFirst(self) :
        yield self
        for c in self :
            yield from c.depthFirst()


if __name__ == '__main__' :
    root = Node(0)
    ch1 = Node(1)
    ch2 = Node(2)
    root.addChild(ch1)
    root.addChild(ch2)
    root.addChild(Node(3))
    root.addChild(Node(4))
    root.addChild(Node('E'))

    print('Depth first search :')
    for ch in root.depthFirst() : 
        print(ch)


# $ python tut1.py 
# Depth first search :     
# 0
# 1
# 2
# 3
# 4
# E

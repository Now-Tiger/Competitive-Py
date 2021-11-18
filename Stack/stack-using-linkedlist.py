#!/usr/bin/env python3

# ------------------------------ Implement stack using linked-list ---------------------------------------

from typing import List, Optional

class Node(object) :
    def __init__(self, val = None) -> None:
        self.val = val
        self.next = None 

class Stack(object) :
    def __init__(self, head : Optional[Node]) -> Optional[Node] :
        self.head = None 

    def isEmpty(self) -> bool :
        return True if self.head is None else False 

    def push(self, data : int) -> int :  
        newNode = Node(data) 
        newNode.next = self.head
        self.head = newNode
        print(f'{data} pushed into the stack')

    def pop(self) :
        if self.isEmpty() :
            raise IndexError('Pop from empty stack !!')
        temp = self.head 
        self.head = self.head.next
        popped = temp.val  
        return popped 

    def peek(self) :
        if self.isEmpty() :
            print('stack is empty !')
        print(self.head.val) 

    def printStack(self) :
        if self.head is None :
            return self.head 
        current = self.head 
        while current :
            print(current.val, end = ' -> ')
            current = current.next
        print(None)
    
    def reverse(self) :
        # -----------------------------------------------------|
        # Additional method to play around                     |
        # what if interviewer asked you to reverse this stack. |
        # ---------------------------------------------------- |
        prev = None 
        current = self.head 
        while current is not None :
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__' :
    stack = Stack(None)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.printStack()
    stack.peek()
    stack.pop()
    stack.printStack()
    #print(stack.isEmpty())
    stack.reverse()
    stack.printStack()
    stack.pop()
    stack.printStack()   

# $ Alienware-Aw27 👘
# 10 pushed into the stack
# 20 pushed into the stack
# 30 pushed into the stack
# 30 -> 20 -> 10 -> None  
# 30
# 20 -> 10 -> None        
# 10 -> 20 -> None        
# 20 -> None
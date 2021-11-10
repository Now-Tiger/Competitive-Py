#!/usr/bin/env python3

# ------------------------------------- 206. Reverse Linked List ------------------------------------
#
#   Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
# Example 1 :
#
#   1  ->  2  ->  3  ->  4  ->  5  
#                 |
#                 v
#   5  ->  4  ->  3  ->  2  ->  1 
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
#
# Example 2 :
# Input: head = [1,2]
# Output: [2,1]
#
# ----------------------------------------------------------------------------------------------------

from typing import Optional

class Node(object) :
    def __init__(self, val = 0, next = None) :
        self.val = val
        self.next = next 

class Solution :
    def revese(self, head : Optional[Node]) -> Optional[Node] :
        prev = None
        current = head
        while current :
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

# ----------------- Using Stack : This one is not an ideal solution -------------------
#  REASON :
#           Because if the stack is empty / linked list is empty code raises the error.
#  This solution might be good to come up with as a naive solution in an interview
#  Then you can tell this solution is not ideal, and you have above solution that
#  can resolve the problem. This way you can build your profile.
# 
#  You can use the last solution as well.


from typing import Optional

class Node(object) :
    def __init__(self, val = 0, next = None) :
        self.val = val
        self.next = next 

class Solution :
    def revese(self, head : Optional[Node]) -> Optional[Node] :
        stack = []
        temp = head
        while temp :
            stack.append(temp)
            temp = temp.next
        head = temp = stack.pop()
        # Untill stack is not 'empty'
        while len(stack) > 0 :
            data = stack.pop()
            temp.next = data
            temp = data
        data.next = None
        return head

    def printList(self, head) :
        if head is None :
            return head
        current = head
        while current :
            print(current.val, end = '->')
            current = current.next
        print('null')

# ----------------------------------------------------------------------------------------------------

from typing import Optional

class Node(object) :
    def __init__(self, val) :
        self.val = val
        self.next = None 

class Linkedlist :
    def __init__(self, head : Optional[Node]) -> Optional[Node] :
        self.head = head
    
    def reverse(self) :
        prev = None
        current = self.head
        while current is not None :
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
         
    def push(self, data) :
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self) :
        if self.head is None :
            return self.head
        current = self.head
        while current :
            print(current.val, end = '->')
            current = current.next
        print('null')

if __name__ == '__main__' :
    list = Linkedlist(None)
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    list.push(5)
    list.printList()
    list.reverse()
    list.printList()

# $ python linked-lists/reverse-linkedlist.py       
# 5->4->3->2->1->null
# 1->2->3->4->5->null
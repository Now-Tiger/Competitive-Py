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
         
    '''
      - This function inserts elements like when you pop out all elements 
    from a stack on by one. 
      - If you use push function you have to make changes
    in driver function.
    ---------------------------------------------------------------------------
    Ex. After inserting all the elements into the linked list it would look
        like this : 5->4->3->2->1->null
        Then you'll reverse it using reverse fucntion.
        seems lil odd  !!
    ---------------------------------------------------------------------------
    def push(self, data) :
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
        '''

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
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    Fifth = Node(5)
    list.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = Fifth

    list.printList()
    list.reverse()
    list.printList()

# $ python linked-lists/reverse-linkedlist.py       
# 1->2->3->4->5->null
# 5->4->3->2->1->null

#!/usr/bin/ pypy3

from __future__ import annotations, division
from typing import Optional


class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def middle(self) -> int:
        """
        Approach 1:
            Traverse linked list using two pointers. 
            Move one pointer by one and the other pointers by two. 
            When the fast pointer reaches the end slow pointer 
            will reach the middle of the linked list.
        """
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        print(f'Middle element = {slow.data}')

    def middle_element(self) -> int :
        """
        Approach 2:
            Initialize mid element as head and initialize a counter as 0. 
            Traverse the list from head, while traversing increment the counter 
            and change mid to mid->next whenever the counter is odd. 
            So the mid will move only half of the total length of the list.
        """
        counter = 0
        mid = self.head
        heads = self.head
        while heads != None :
            if counter & 1 :
                mid = mid.next
            counter += 1
            heads = heads.next
        # if empty list is provided :
        if mid != None :
            print(f"Middle element = {mid.data}")

    def printlist(self) -> str:
        current = self.head
        if current.data is None:
            print('Empty linkedlist head')
        while current:
            print(current.data, end='->')
            current = current.next
        print(None)

    def size(self) -> int:
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        print(f'size = {counter}')


if __name__ == '__main__':
    list = LinkedList(None)
    list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    fifth = Node(50)

    list.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    list.printlist()
    list.size()
    list.middle()
    list.middle_element()


# $ pypy linked-lists/middle-element.py
# 10->20->30->40->50->None
# size = 5
# Middle element = 30
# Middle element = 30

# Time Complexity : O(n)  | Space complexity : O(1)

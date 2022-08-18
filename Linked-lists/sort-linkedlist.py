#!/use/bin/env/ pypy3
# -*- coding: utf-8 -*-
# ------------------------------------ Sort given linked list in ascending order ------------------------------------ #

from collections import deque

class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)

    return head

def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.val, end="-> ")
        ptr = ptr.next
    print('None')


class Solution:
    def solve(self, node):
        values = []
        head = node
        while node:
            values.append(node.val)
            node = node.next

        values.sort()
        values = deque(values)

        node = head
        while node:
            node.val = values.popleft()
            node = node.next

        return head


ob = Solution()
head = make_list([5, 8, 4, 1, 5, 6, 3])
print('Given linked list :')
print_list(head)
print('-------------------\nAfter sorting linked list :')
print_list(ob.solve(head))


# $ python sort-linkedlist.py 
# Given linked list :
# 5-> 8-> 4-> 1-> 5-> 6-> 3-> None
# -------------------
# After sorting linked list :     
# 1-> 3-> 4-> 5-> 5-> 6-> 8-> None

# T.C = O(n)


#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# ------------------- Remove duplicates from a sorted linked list -------------------
# Write a function that takes a list sorted in non-decreasing order and
# deletes any duplicate nodes from the list.
# The list should only be traversed once.
# For example if the linked list is 11->11->11->21->43->43->60
# then remove_duplicates() should convert the list to 11->21->43->60.
# -----------------------------------------------------------------------------------

from __future__ import annotations
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Linkedlist(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def remove_duplicates_efficient(self) -> None:
        """
            function removes duplicate elements
            traversing through list and comparing
            next element.
            -------------------------------------
            T.C: O(n) visiting all nodes.
            S.C: O(1) no extra space used
        """
        current = self.head
        if current == None and current.next == None:
            return 0
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            current = current.next
        return

    def remove_duplicates(self) -> None:
        """
            This method takes an extra 
            space as dictionary to check
            duplicates.
            ---------------------------
            S.C = O(n)
        """
        current = self.head
        prev = None
        duplicates = {}
        while current.next:
            if current.data not in duplicates:
                duplicates[current.data] = None
                prev = current
            else:
                prev.next = current.next

            current = current.next
        return

    def remove(self) -> None:
        curr = self.head
        if curr is None:
            return 0
        while curr.next:
            temp = curr
            while (temp.data != None and temp.data == curr.data):
                temp = temp.next
            curr.next = temp
            curr = curr.next
        return

    def insert(self, value: int) -> None:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def printlist(self) -> str:
        current = self.head
        while current != None:
            print(current.data, end="->")
            current = current.next
        print(None)


if __name__ == "__main__":
    lis = Linkedlist(None)
    lis.insert(11)
    lis.insert(11)
    lis.insert(12)
    lis.insert(13)
    lis.insert(15)
    lis.printlist()
    lis.remove_duplicates_efficient()
    # lis.remove_duplicates()
    # lis.remove()
    lis.printlist()

# $ pypy3 linked-lists/remove-duplicates-new.py
# 11->11->12->13->15->None
# 11->12->13->15->None

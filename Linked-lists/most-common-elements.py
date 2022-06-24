#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Python program to find most common elements of a linked list.
# These are several approaches; whihc are extremely bad and messy, basically not efficient.

from __future__ import annotations
from collections import Counter
from typing import Optional


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def insert(self, data) -> None:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def repeated_elements(self) -> list:
        current = self.head
        counter = {}
        while current:
            if current.data in counter:
                counter[current.data] += 1
            else:
                counter[current.data] = 1
            current = current.next
        return [key for key in counter.keys()
                if
                counter[key] == max(counter.values())
                ]

    def first_common_element(self) -> list:
        dups = []
        current = self.head
        while current:
            dups.append(current.data)
            current = current.next
        return Counter(dups).most_common(1)[0][0]

    def printlist(self) -> str:
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print(None)


if __name__ == "__main__":
    lis = LinkedList(None)
    lis.insert(5)
    lis.insert(5)
    lis.insert(4)
    lis.insert(3)
    lis.insert(3)
    lis.insert(2)
    lis.insert(2)
    lis.insert(1)

    print("given linked list:")
    lis.printlist()
    print(f"repeated elements: {lis.repeated_elements()}")
    print(f"first common element: {lis.first_common_element()}")

# $ pypy3 linked-lists/most-common-elements.py
# given linked list:
# 5->5->4->3->3->2->2->1->None
# repeated elements: [5, 3, 2]
# first common element: 5

#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

from typing import Optional


class Node(object):
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def insert(self, data: int) -> Node:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def printlist(self) -> int:
        current = self.head
        if current.data is None:
            print("Head is empty")
            return
        while current != None:
            print(current.data, end="->")
            current = current.next
        print('None')

    def kth_element_from_end(self, key) -> int:
        fast = slow = self.head
        count: int = 0

        if key == 0 or key is None:
            print(f"enter proper key: {key}")
            return

        if self.head is not None:
            while count < key:
                if slow is None:
                    print(f"{key} is greater than number of nodes in list")
                    return
                slow = slow.next
                count += 1

        if slow is None:
            next = self.head.next
            if next is not None:
                print(f"Node {key} from last is {fast.data}")
        else:
            while slow is not None:
                fast = fast.next
                slow = slow.next
            print(f"Node {key} from last is {fast.data}")


if __name__ == "__main__":
    list = LinkedList(None)

    elements = [10, 55, 3, 88, 99, 5, 63, 92, 1000]
    for element in elements:
        list.insert(element)

    list.printlist()
    list.kth_element_from_end(5)


# $ pypy3 Kth-node-from-end.py
# 10->55->3->88->99->5->63->92->1000->None
# element 5 from last is 99

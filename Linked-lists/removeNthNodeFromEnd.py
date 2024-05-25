#!/usr/bin/env python3
from __future__ import annotations
from typing import Optional

# TODO: Remove nth node from the end of the LinkedList


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


class LinkedList(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def insert(self, data: int) -> None:
        if self.head:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)


def display(root: Optional[Node]) -> None:
    while root is not None:
        print(root.data, end="->")
        root = root.next
    print(None)


def remove_node_bruteforce(head: Optional[Node], position: int) -> Optional[Node]:
    """T.C: O(2(len)) | S.C: O(1)"""
    length: int = 0
    current = head

    # Count the length of the linkedlist
    while current is not None:
        length += 1
        current = current.next

    # if it the head of linkedlist that has been asked to delete
    if length == position and head is not None:
        new_head = head.next
        head = None
        return new_head

    result = length - position  # 6 - 2 = 4 <- indexed element/node needs to be deleted
    temp = head

    while temp is not None:
        result -= 1
        if result == 0:
            break
        temp = temp.next

    # Delete the nth node from the end
    if temp is not None:
        delete_node = temp.next
        temp.next = temp.next.next
        delete_node = None
    return head


def optimized_pointers(head: Optional[Node], position: int) -> Optional[Node]:
    fastp = slowp = head

    for _ in range(position):
        fastp = fastp.next

    if fastp is None:
        new_head = head.next
        head = None
        return new_head

    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    delelte_node = slowp.next
    slowp.next = slowp.next.next
    delelte_node = None

    return head


def main() -> None:
    data = [1, 3, 4, 5, 1, 6]
    L = LinkedList(None)
    for num in data:
        L.insert(num)

    print("Original Linkedlist: ")
    display(L.head)

    print("Modified Linkedlist: ")
    h = optimized_pointers(L.head, 2)
    display(h)


if __name__ == "__main__":
    main()

# python3 removeNthNodeFromEnd.py
# Optional Linkedlist
# 1->3->4->5->1->6->None
# Modified Linkedlist
# 1->3->4->5->6->None

#!/usr/bin/env/ pypy3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Optional

""" Question: Check if given linkedlist is polindrome or not.
    Ex. 1: 1->2->3->2->1 : True
        2: 5->4->3->2->4 : False
"""


class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head

    def efficient_approach(self) -> bool:
        """ Built in method for LinkedList class, implements \
        two pointer approach.
        `NOT A GOOD PRACTICE THO`
        - FIX THE BUG OF THIS METHOD **ASAP**
        --------
        Time Complexity: O(n)
        Space Complexity: O(1)

        Returns:
        --------
        bool: True if the linkedlist is Polindrome else False.
        """
        slow = self.head
        fast = self.head
        if self.head is None and self.head.next is None:
            return True
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        # slow pointer is pointing to the middle element,
        # so reversing the list after the middle element.
        slow.next = self.reverse_helper(slow.next)
        slow = slow.next
        temp = self.head

        while slow != None:
            if temp.data != slow.data:
                return False
            temp = temp.next
            slow = slow.next
        return True

    def naive_polindrome(self) -> bool:
        """ Naive approach
            returns boolean value.
            --------------------------
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        stack = []
        current = self.head
        is_polindrome = True
        while current is not None:
            stack.append(current.data)
            current = current.next
        while self.head is not None:
            i = stack.pop()
            if self.head.data == i:
                is_polindrome = True
            else:
                is_polindrome = False
                break
            self.head = self.head.next
        return is_polindrome

    def second_approach(self) -> None:
        """ This is also a naive approach 
            -----------------------------
            - Save all the nodes in an array.
            - Reverse the original linkedlist.
            - Compare current node with current index array value.
            - if both values are same, shift to next element in both
              else return False as list is not polindrome.
            - Continue above steps until entire list is traversed or
              until a missmach is found!
        """
        i = 0
        array = []
        current = self.head
        if self.head is None:
            print("Empty head node!")
            return
        while current is not None:
            array.append(current.data)
            current = current.next
        self.reverse_helper(self.head)
        curr = self.head
        while curr is not None:
            if curr.data != array[i]:
                return False
            curr = curr.next
            i += 1
        return True

    def reverse_helper(self, head: Node) -> Node:
        prev = None
        next = None
        curr = head
        if head is None:
            print(f"head is empty!")
            return
        while curr is not None:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        self.head = prev

    def insert(self, val: int) -> None:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)
        else:
            self.head = Node(val)

    def printlist(self) -> None:
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print(None)


def main() -> None:
    List = LinkedList(None)
    string = 'racecar'
    # arr1 = [1, 2, 3, 2, 1]
    # arr2 = [5, 4, 3, 4, 1]
    for elem in string:
        List.insert(elem)

    List.printlist()
    ans = List.efficient_approach()
    print(ans)
    del List, string, ans


if __name__ == "__main__":
    main()

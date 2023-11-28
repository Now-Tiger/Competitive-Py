#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List

__author__ = "Swapnil Narwade"
__version__ = "0.0.1"
__license__ = "GPL"


"""Problem: Check if given array of integers is sorted or not. """


def is_sorted_iterative(array: List[int]) -> bool:
    """Optimal than the recussive implementation"""
    if len(array) == 1:
        return True
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1] and array[i] != array[i + 1]:
            # displays where condition is failed.
            print(f">> {array[i]} -> {array[i + 1]}")
            return False
    return True


def is_sorted_recursive(array: List[int]) -> bool:
    """Recursive implementation of the solution"""
    if len(array) == 1:
        return True
    return array[0] <= array[1] and is_sorted_recursive(array[1:])


def main() -> None:
    test_case_one = [1, 2, 3, 4, 5, 5, 99, 3]
    test_case_sec = [-1, -1, -1, -1, 2, 3, 4]

    print(f">> {test_case_one}")
    result = is_sorted_iterative(array=test_case_one)
    print(f">> {result}")

    print("--------------------------------")

    print(f">> {test_case_sec}")
    result = is_sorted_iterative(array=test_case_sec)
    print(f">> {result}")

    return


if __name__ == "__main__":
    main()

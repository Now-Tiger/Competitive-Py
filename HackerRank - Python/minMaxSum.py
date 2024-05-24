#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__question__ = """
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly 
four of the five integers. Then print the respective minimum and maximum values as a single line of two 
space-separated long integers.

Example
arr = [1, 3, 5, 7, 9]

The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24 The function prints `16 24`
"""


def min_max_sum_naive(arr: list[int]) -> None:
    """naive / brute force solution
    T.C: O(n) | S.C: O(n)
    """
    min_elements = list()
    max_elements = list()
    copy = arr.copy()
    for i in range(4):
        min_elem = min(arr)
        arr.remove(min_elem)
        min_elements.append(min_elem)

        max_elem = max(copy)
        copy.remove(max_elem)
        max_elements.append(max_elem)
        if i == 4:
            break
    print(sum(min_elements), sum(max_elements))


def min_max_sum_better(arr: list[int]) -> None:
    """T.C: (n^2) | S.C: O(1)"""
    min_sum = float("inf")
    max_sum = float("-inf")

    for i in range(len(arr)):
        current_sum = sum(arr) - arr[i]
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum

    print(min_sum, max_sum)


def min_max_sum_optimized(arr: list[int]) -> None:
    """T.C: O(n) | S.C: O(1)"""
    min_element = min(arr)
    max_element = max(arr)

    min_sum = sum(arr) - max_element
    max_sum = sum(arr) - min_element
    print(min_sum, max_sum)


def main() -> None:
    # arr = [1, 3, 5, 7, 9]
    arr = [1, 2, 3, 4, 5]
    min_max_sum_optimized(arr=arr)


if __name__ == "__main__":
    main()

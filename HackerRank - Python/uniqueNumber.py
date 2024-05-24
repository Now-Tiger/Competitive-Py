#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations


__problem__ = """ 
Given an array of integers, where all elements but one occur twice, find the unique element.
Example
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.

Function Description
--------------------
Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

* int a[n]: an array of integers

Returns
-------
int: the element that occurs only once
"""


def naive_solution(array: list[int]) -> int:
    """T.C: O(n^2) | S.C: O(n)"""
    k = 0
    hashmap: dict[int, int] = dict()
    for i in array:
        hashmap[i] = 0

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                hashmap[array[i]] += 1
    for key, val in hashmap.items():
        if val == 0:
            k = key
    return k


def better_solution(array: list[int]) -> int:
    """T.C: O(n) | S.C: O(n)"""
    unique = -1
    hashmap = dict()
    for num in array:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for num in hashmap:
        if hashmap[num] == 1:
            unique = num
    return unique


def optimized_solution(array: list[int]) -> int:
    """T.C: O(n) | S.C: O(1)"""
    unique = 0
    for num in array:
        unique ^= num
    # -1 represent no unique element
    return -1 if unique == 0 else unique


def main() -> None:
    array = [1, 2, 3, 4, 3, 2, 1]
    res = optimized_solution(array)
    print(res)


if __name__ == "__main__":
    main()

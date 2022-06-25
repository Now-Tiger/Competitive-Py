#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Python program to find repeated elements in a list(array).

from __future__ import annotations
from collections import Counter

def repeated_elements(array: list) -> list:
    counter: dict = {}
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1 
    return [key for key in counter.keys() 
            if 
            counter[key] == max(counter.values())
            ]

def using_lib(array: list) -> None:
    if len(array) == 0:
        print("Enter valid array")
        return
    else:
        values = Counter(array).most_common()
        for key, val in values:
            if val > 1:
                print(key, val, sep = " counts: ")


if __name__ == "__main__":
    array = [4, 5, 3, 2, 1, 2, 5, 1]
    array_new = []
    print(repeated_elements(array))
    using_lib(array)
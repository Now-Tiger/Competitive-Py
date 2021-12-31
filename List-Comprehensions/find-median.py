#!/usr/bin pypy3

# algorithm to find the median of the array containing elements
# write a function.

from __future__ import annotations
from typing import List


def median(data: List[int | float]) -> None:
    n = len(data)
    odd = []
    even = []
    r = (n // 2)
    l = (n // 2) - 1
    med = (data[l] + data[r]) / 2
    odd_med = n // 2

    if n % 2 == 0:
        even.extend(data)
        print(f'even data: {even}')
    else:
        odd.extend(data)
        print(f'odd data: {odd}')

    if even:
        print(f"median: {med}")
        return
    else:
        print(f"median: {data[odd_med]}")
        return


if __name__ == '__main__':
    data = [3, 4, 6, 7.5, 8]
    median(data)
    print('-'*30)

    data = [2, 4, 6, 8, 9.2, 10.2, 11, 12.5]
    median(data)

# $ pypy pypy3/find-median.py
# odd data: [3, 4, 6, 7.5, 8]
# median: 6
# ------------------------------
# even data: [2, 4, 6, 8, 9.2, 10.2, 11, 12.5]
# median: 8.6
#!/usr/bin/ python3
# -*- coding: utf-8 -*-

from __future__ import annotations, division
from collections import Counter as counter
# from statistics import median
from typing import List
import numpy as np


class Statistics(object):
    def __init__(self, arr: List) -> None:
        self.arr = arr

    def mean(self) -> float:
        # total = 0
        # for item in self.arr:             <= for loop is costly
        #     total += item
        # return total / len(self.arr)
        # return np.average(self.arr)
        # return np.mean(self.arr)          <= better
        return sum(self.arr) / len(self.arr)

    def mode(self) -> int:
        # counter: dict = {}                <= takes extra space
        # for item in self.arr:
        #     if item in counter:
        #         counter[item] += 1
        #     else:
        #         counter[item] = 1
        # return [key for key in counter.keys() if counter[key] == max(counter.values())]

        # below return statement would not work if you have numpy array.
        # return max(set(self.arr), key=self.arr.count)
        return counter(self.arr).most_common(1)[0][0]

    def median(self) -> int:
        n = len(self.arr)
        sorted_arr = sorted(self.arr)
        midpoint = n // 2
        if n % 2 == 1:
            return sorted_arr[midpoint]
        else:
            left = midpoint - 1
            right = midpoint
            return (sorted_arr[left] + sorted_arr[right]) / 2
        # return median(self.arr)


if __name__ == "__main__":
    A = [1, 4, 6, 8, 10, 22, 2, 2, 8, 10]
    B = np.array(A)
    # print(B)
    instance = Statistics(B)
    print(f"mean: {instance.mean()}")
    print(f"mode: {instance.mode()}")
    print(f"median: {instance.median()}")

# $ python Stats/mean_mode_median.py
# mean: 7.3
# mode: 8
# median: 7.0

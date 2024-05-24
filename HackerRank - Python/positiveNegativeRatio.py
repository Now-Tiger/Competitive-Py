#!/usr/bin/env python3

""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable.

Example
ar = [1, 1, 0, -1, -1]
There are  elements, two positive, two negative and one zero. 
Their ratios are 2/5=0.400000, 2/5=0.400000 and 1/5=0.200000 Results are printed as:

0.400000
0.400000
0.200000
"""


def ratios(array: list[int]) -> None:
    positives: int = 0
    negatives: int = 0
    zeros: int = 0
    total: int = len(array)

    for num in array:
        if num < 0:
            negatives += 1
        elif num == 0:
            zeros += 1
        else:
            positives += 1

    positive_ratio: float = round(positives / total, 6)
    negative_ratio: float = round(negatives / total, 6)
    zeros_ratio: float = round(zeros / total, 6)
    print(positive_ratio, negative_ratio, zeros_ratio, sep="\n")


ratios(array=[1, 1, 0, -1, -1])

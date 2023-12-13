#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Swapnil Narwade"
__description__ = """Implementation of selection sort algorithm"""
__version__ = "0.0.1"


def selection_sort(array: list[int]) -> list[int]:
    for i in range(len(array)):
        min_element = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_element]:
                min_element = j

        array[i], array[min_element] = array[min_element], array[i]
    return array


def main() -> None:
    array = [3, 4, 5, 88, 0, 1, 2]
    print(f">> given array: {array}")
    sorted_array = selection_sort(array)
    print(f">> Sorted array: {sorted_array}")
    return


if __name__ == "__main__":
    main()

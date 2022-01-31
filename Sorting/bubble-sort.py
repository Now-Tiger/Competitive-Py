#!/usr/bin pypy3

# ---------------------------------------- Bubble Sort ----------------------------------------

import numpy as np
from typing import List

def bubble_sort(array: List[int or float]) -> None :
    for i in range(len(array)-1, 0, -1) :
        for j in range(i) :
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]



# Above method takes O(n^2) time complexity even in best case 
# Below is the modified version

def bubble(array: List[int or float]) -> None :
    '''
        This modified version improves the 
        best case of bubble sort to O(n)
    '''
    swapped = 1
    for i in range(len(array)-1, 0, -1) :
        if swapped == 0 :
            return
        for j in range(i) :
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                swapped = 1


if __name__ == "__main__" :
    array: List[int] = [10, 4, 43, 5, 57, 91, 45, 7]
    print(f"Original array : {array}")
    bubble_sort(array)
    print(f"Sorted array : {array}")

    b: np.ndarray = np.random.randint(10, size = 10)
    print(b)
    bubble_sort(b)
    print(b)

    # ----------------------------------------------------

    c: List[int] = [10, 4, 43, 5, 57, 91, 45, 7]
    print(f"Original array : {c}")
    bubble(c)
    print(f"Sorted array : {c}")
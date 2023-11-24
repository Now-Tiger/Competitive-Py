#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Problem: Find second largest element in the array of integers.


class Solution(object):
    def naive(self, array: list[int]) -> int:
        """Assumes that the given array is sorted"""
        return array[-2]

    def okayish(self, array: list[int]) -> int:
        """
        Fails in such scenarios where an
        array contains duplicate elements at
        the end
        """
        counter = 0
        second_largest = array[0]
        for i in array:
            if i > second_largest:
                second_largest = i
                counter += 1

                if counter == len(array) - 2:
                    break
        return second_largest

    def better(self, array: list[int]) -> int:
        """
        Assumes given array is sorted. Althoguh
        handles the problem of duplicate elements
        """
        array.sort()
        current = array[0]
        largest = array[-1]
        for i in array:
            if i > current and i < largest:
                current = i
        return current

    def much_better(self, array: list[int]) -> int:
        largest = array[0]
        second_largest = -1
        for i in array:
            if i > largest:
                largest = i
        for i in array:
            if i > second_largest and i < largest:
                second_largest = i
        return second_largest

    def efficient(self, array: list[int]) -> int:
        largest = array[0]
        second_largest = -1
        for i in array:
            if i > largest:
                second_largest = largest
                largest = i
            elif i < largest and i > second_largest:
                second_largest = i
        return second_largest


def main() -> None:
    # test_case_1 = [1, 2, 3, 4, 5]
    # test_case_2 = [2, 3, 4, 5, 5]
    # test_case_3 = [1, 7, 7, 7, 7]
    test_case_4 = [1, 10, -1, -7, 88, 88, 2, 9]
    print(test_case_4)
    instance = Solution()
    result_test_case_4 = instance.efficient(array=test_case_4)
    print(result_test_case_4)


if __name__ == "__main__":
    main()

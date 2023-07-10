#!/usr/bin/env/ python3
# coding: utf-8 -*-

from typing import List


class Solution(object):
    def naivesolution(self, numbers: List[int], target: int) -> List[int]:
        if numbers == None or len(numbers) < 2:
            return [-1, -1]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
        return []

    def binary_search(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        numbers.sort()

        if numbers == None or len(numbers) < 2:
            return [-1, -1]
        while (start < end):
            total = numbers[start] + numbers[end]
            if total == target:
                return [start, end]
            if target > total:
                start += 1
            else:
                end -= 1
        return []

    def hash_table(self, numbers: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(numbers):
            remaining = target - num
            if remaining in hashtable:
                return [i, hashtable[remaining]]
            else:
                hashtable[num] = i


def main() -> None:
    instance = Solution()
    numbers = [5, 7, 6, 2, 1, -1, -6, 18, 0]
    target = 99
    res = Solution.hash_table(instance, numbers, target)
    print(res)


if __name__ == "__main__":
    main()

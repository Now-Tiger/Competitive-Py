#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from twosum import Solution
import unittest


class TestTwosum(unittest.TestCase):
    # numbers: list = [5, 7, 6, 2, 1, -1, -6, 18, 0]
    target: int = 12
    instance = Solution()

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_naive_solution(self) -> unittest:
        """ Function iterates array two times increases time complexity """
        self.assertEqual(Solution.naivesolution(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], self.target),
            [0, 1])

    def test_binary_search(self) -> unittest:
        """ Array gets sorted here. Optimized solution"""
        self.assertEqual(Solution.binary_search(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], self.target),
            [0, 8])
        self.assertEqual(Solution.binary_search(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], 0),
            [0, 6])

    def test_hash_table(self) -> unittest:
        """ Optimized alternative O(n) to above two solution, thus takes extra space."""
        self.assertEqual(Solution.hash_table(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], self.target),
            [1, 0])
        self.assertEqual(Solution.hash_table(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], 0),
            [5, 4])
        self.assertEqual(Solution.hash_table(
            self.instance, [5, 7, 6, 2, 1, -1, -6, 18, 0], 99),
            None)


if __name__ == "__main__":
    unittest.main()

    # >> python -m unittest -v twosumtest.py
    # test_binary_search (twosumtest.TestTwosum.test_binary_search) ... ok
    # test_naive_solution (twosumtest.TestTwosum.test_naive_solution) ... ok

    # ----------------------------------------------------------------------
    # Ran 2 tests in 0.000s

    # OK

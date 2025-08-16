#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Swapnil Narwade
Email: swapnil.narwade3@gmail.com
Problem: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""
from __future__ import annotations


def find_path(matrix: list[list[int]]) -> list[str]:
    path_str = ""
    n = len(matrix)
    ans: list[str] = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    helper(matrix, 0, 0, ans, path_str, visited)

    return ans


def helper(
    matrix: list[list[int]],
    row: int,
    col: int,
    ans: list[str],
    path_str: str,
    visited: list[list[bool]],
) -> None:

    n = len(matrix)

    if (
        row < 0
        or col < 0
        or row >= n
        or col >= n
        or (matrix[row][col] == 0)
        or visited[row][col] is True
    ):
        return

    if row == n - 1 and col == n - 1:
        ans.append(path_str)
        return

    visited[row][col] = True

    # Moving in the directions (safely)
    if row > 0:
        helper(matrix, row - 1, col, ans, path_str + "U", visited)  # UP
    if row < n - 1:
        helper(matrix, row + 1, col, ans, path_str + "D", visited)  # DOWN
    if col < n - 1:
        helper(matrix, row, col + 1, ans, path_str + "R", visited)  # Right
    if col > 0:
        helper(matrix, row, col - 1, ans, path_str + "L", visited)  # Left

    visited[row][col] = False


def main() -> None:
    n = 4
    mat = [[0 for _ in range(n)] for _ in range(n)]

    mat[0][0] = 1
    mat[1][0] = 1
    mat[1][1] = 1
    mat[1][2] = 1
    mat[1][3] = 1
    mat[2][0] = 1
    mat[2][1] = 1
    mat[2][3] = 1
    mat[3][1] = 1
    mat[3][2] = 1
    mat[3][3] = 1

    print("::: Maze Path :::")
    for rows in mat:
        for elem in rows:
            print(f"{elem} ", end=" ")

        print()

    print("::: Calculated paths :::")
    paths = find_path(mat)
    for path in paths:
        print(f"{path},", end=" ")

    print()

    # ::: Maze Path :::
    # 1  0  0  0
    # 1  1  1  1
    # 1  1  0  1
    # 0  1  1  1
    # ::: Calculated paths :::
    # DDRURRDD, DDRDRR, DRDDRR, DRRRDD,

    return


if __name__ == "__main__":
    main()

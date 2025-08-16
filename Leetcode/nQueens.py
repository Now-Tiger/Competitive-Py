#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Swapnil Narwade
Email: swapnil.narwade3@gmail.com
Problm: https://leetcode.com/problems/n-queens/description/
"""
from __future__ import annotations
from typing import Optional


class Solution(object):
    def __init__(self, board: Optional[list[list[int]]] = None) -> None:
        self.board = board

    def is_safe(self, board: list[list[int]], row: int, col: int) -> bool:
        # 1. Vertical/Row wise check
        for i in range(row):
            if board[i][col] == 1:
                return False

        # 2. Positive diagonal check
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # 3. Negative diagonal check
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def move_queen(self, row: int) -> None:
        if not self.board:
            return

        if row == len(self.board[0]):
            self.print_board()
            return

        for col in range(len(self.board[0])):
            if self.is_safe(self.board, row, col):
                self.board[row][col] = 1
                self.move_queen(row + 1)
                self.board[row][col] = 0

    def print_board(self) -> None:
        if not self.board:
            return

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                print(self.board[row][col], end="  ")

            print()

        print("-" * 10)


def main() -> None:
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]
    instance = Solution(board)
    instance.move_queen(0)


if __name__ == "__main__":
    main()
